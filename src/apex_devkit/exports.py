"""Never execute export SQL. Only count recognized component declarations."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import re
import zipfile
import stat
from .analysis import Finding, mask_sql

MAX_BYTES = 20 * 1024 * 1024
MAX_MEMBERS = 1000

COMPONENTS = {
    'create_page': 'pages',
    'create_page_item': 'page_items',
    'create_page_button': 'buttons',
    'create_page_plug': 'regions',
    'create_page_da_event': 'dynamic_actions',
    'create_security_scheme': 'authorization_schemes',
    'create_list_of_values': 'shared_lovs',
    'create_page_process': 'page_processes',
}
CALL = re.compile(r'\bwwv_flow_imp(?:_page|_shared)?\s*\.\s*(create_[a-z_]+)\s*\(', re.I)


def inspect_text(source: str, path: str) -> tuple[Counter, list[Finding]]:
    # Comments are removed to avoid interpreting commented-out calls.
    text = mask_sql(source)
    counts = Counter()
    findings = []
    for m in CALL.finditer(text):
        name = m.group(1).lower()
        if name in COMPONENTS:
            counts[COMPONENTS[name]] += 1
    # APEX export settings vary by version and exporter; this is a review prompt only.
    for m in re.finditer(r'\bp_authentication_id\s*=>\s*null\b', text, re.I):
        findings.append(Finding('APEX001', 'low', path, source.count('\n', 0, m.start()) + 1,
            'Authentication configuration appears unset in an export declaration',
            'Review application authentication in APEX App Builder; export context may be incomplete.'))
    return counts, findings


def _safe_zip_members(zf: zipfile.ZipFile):
    members = zf.infolist()
    if len(members) > MAX_MEMBERS:
        raise ValueError('ZIP has too many members')
    if sum(i.file_size for i in members) > MAX_BYTES:
        raise ValueError('ZIP uncompressed size limit exceeded')
    for member in members:
        p = Path(member.filename)
        unix_mode = (member.external_attr >> 16) & 0xFFFF
        if stat.S_ISLNK(unix_mode):
            raise ValueError('ZIP symlinks are not accepted')
        if member.flag_bits & 1:
            raise ValueError('Encrypted ZIP members are not accepted')
        if (not member.filename or p.is_absolute() or '..' in p.parts
                or '\\' in member.filename or ':' in p.parts[0]):
            raise ValueError('Unsafe archive path')
        if member.is_dir() or not member.filename.lower().endswith('.sql'):
            continue
        yield member


def _read_bounded(zf: zipfile.ZipFile, member: zipfile.ZipInfo, remaining: int) -> str:
    # Cap ACTUAL decompressed bytes, not just untrusted ZIP metadata.
    with zf.open(member) as stream:
        raw = stream.read(min(remaining, MAX_BYTES) + 1)
    if len(raw) > remaining:
        raise ValueError('ZIP actual uncompressed size limit exceeded')
    return raw.decode('utf-8-sig')


def inspect_export(path: Path) -> dict:
    counts = Counter()
    findings = []
    files = 0
    def read_sql(text: str, name: str):
        nonlocal files
        files += 1
        c, f = inspect_text(text, name)
        counts.update(c)
        findings.extend(f)

    if path.is_file() and path.suffix.lower() == '.zip':
        with zipfile.ZipFile(path) as zf:
            remaining = MAX_BYTES
            for member in _safe_zip_members(zf):
                decoded = _read_bounded(zf, member, remaining)
                remaining -= len(decoded.encode('utf-8-sig'))
                read_sql(decoded, member.filename)
    elif path.is_file() and path.suffix.lower() == '.sql':
        if path.stat().st_size > MAX_BYTES:
            raise ValueError('File size limit exceeded')
        read_sql(path.read_text(encoding='utf-8-sig'), path.name)
    elif path.is_dir():
        paths = sorted(path.rglob('*.sql'))
        if len(paths) > MAX_MEMBERS or sum(p.stat().st_size for p in paths) > MAX_BYTES:
            raise ValueError('Export exceeds configured size limits')
        for file in paths:
            if file.is_symlink() or any(parent.is_symlink() for parent in file.parents if parent != path.parent):
                raise ValueError('Symlinks are not accepted')
            read_sql(file.read_text(encoding='utf-8-sig'), str(file.relative_to(path)))
    else:
        raise ValueError('Supply an SQL file, ZIP archive, or directory')
    return {'kind': 'apex-export', 'files_inspected': files, 'components': dict(sorted(counts.items())),
            'findings': [f.to_dict() for f in findings],
            'limitations': 'Conservative signature counts only; not a full APEX parser or vulnerability assessment.'}
