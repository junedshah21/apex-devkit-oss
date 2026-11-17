from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
from .analysis import RULES, analyze_sql
from .exports import inspect_export, MAX_BYTES


def to_markdown(report: dict) -> str:
    lines = ['# APEX DevKit OSS report', '', f"Inspection: `{report['kind']}`", '']
    if 'components' in report:
        lines += ['## Components', '']
        lines += [f'- {k}: {v}' for k, v in report['components'].items()] or ['None recognized']
        lines += ['', f"Files inspected: {report['files_inspected']}"]
    lines += ['', '## Advisory findings', '']
    for f in report['findings']:
        lines.append(f"- **{f['severity']} {f['rule']}** `{f['path']}:{f['line']}` — {f['message']} {f['suggestion']}")
    if not report['findings']:
        lines.append('No matching advisory patterns (not a security certification).')
    lines += ['', '## Limitations', '', report['limitations'], '']
    return '\n'.join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='apex-devkit', description='Offline, read-only Oracle APEX source analysis')
    sub = parser.add_subparsers(dest='command', required=True)
    lint = sub.add_parser('lint', help='Conservative SQL/PLSQL lexical checks')
    lint.add_argument('file', type=Path)
    lint.add_argument('--disable', action='append', default=[], choices=sorted(RULES))
    exp = sub.add_parser('inspect-export', help='Inspect single/split SQL exports or ZIP')
    exp.add_argument('file', type=Path)
    for cmd in (lint, exp):
        cmd.add_argument('--format', choices=('json', 'markdown'), default='markdown')
        cmd.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'lint':
            if args.file.suffix.lower() != '.sql' or args.file.stat().st_size > MAX_BYTES:
                raise ValueError('SQL input required, at most 20 MiB')
            source = args.file.read_text(encoding='utf-8-sig')
            report = {'kind': 'sql-static', 'findings': [x.to_dict() for x in analyze_sql(source, str(args.file), set(args.disable))],
                'limitations': 'Lexical heuristics only: Semantic parsing, full data flow, and runtime behavior are not assessed.'}
        else:
            report = inspect_export(args.file)
        result = json.dumps(report, indent=2, sort_keys=True) + '\n' if args.format == 'json' else to_markdown(report)
        if args.output:
            args.output.write_text(result, encoding='utf-8')
        else:
            print(result, end='')
        return 0
    except (OSError, ValueError, UnicodeError, __import__('zipfile').BadZipFile) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
