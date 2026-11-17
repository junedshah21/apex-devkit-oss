"""Conservative lexical checks, NOT a SQL or PL/SQL parser.

Mask comments and literals while preserving line boundaries and character offsets.
The analyzer intentionally avoids conclusions about runtime exploitability.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
import re


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str
    suggestion: str
    confidence: str = "low"

    def to_dict(self) -> dict:
        return asdict(self)


def mask_sql(source: str) -> str:
    """Mask comments and SQL literals without changing offsets or newlines.

    Supports Oracle alternative quoting (q'[...]', q'{...}', q'(...)',
    q'<...>', and q'!...!') as well as regular literals, quoted
    identifiers, line comments and block comments. This is a lexer,
    not a semantic SQL/PLSQL parser.
    """
    out = list(source)
    n = len(source)
    i = 0
    pairs = {'[': ']', '{': '}', '(': ')', '<': '>'}
    while i < n:
        start = i
        if source.startswith('--', i):
            end = source.find('\n', i)
            j = n if end == -1 else end
        elif source.startswith('/*', i):
            end = source.find('*/', i + 2)
            j = n if end == -1 else end + 2
        elif (source[i:i+2].lower() == "q'" and i + 2 < n
              and (i == 0 or not (source[i-1].isalnum() or source[i-1] in '_$#'))):
            delim = source[i+2]
            closer = pairs.get(delim, delim)
            end = source.find(closer + "'", i + 3)
            j = n if end == -1 else end + 2
        elif source[i] in "'\"":
            quote = source[i]
            j = i + 1
            while j < n:
                if source[j] == quote:
                    if j + 1 < n and source[j + 1] == quote:
                        j += 2
                        continue
                    j += 1
                    break
                j += 1
        else:
            i += 1
            continue
        for k in range(start, j):
            if out[k] != '\n':
                out[k] = ' '
        i = j
    return ''.join(out)


RULES = {
    'SQL001': ('medium', 'SELECT * can increase coupling and data transfer', 'Select only required columns.'),
    'SQL002': ('low', 'Row-by-row cursor loop warrants review', 'Consider set-based SQL or BULK COLLECT/FORALL after measuring.'),
    'SEC001': ('medium', 'Dynamic SQL construction warrants manual review', 'Use bind variables; allowlist identifiers via DBMS_ASSERT where appropriate.'),
    'SEC002': ('medium', 'WHEN OTHERS handler may conceal errors', 'Log safely and re-raise unless the exception is intentionally handled.'),
    'SQL003': ('low', 'COMMIT inside a PL/SQL routine warrants review', 'Document transaction ownership; normally let the caller decide.'),
}

PATTERNS = {
    'SQL001': re.compile(r'\bSELECT\s*\*\s+FROM\b', re.I),
    'SQL002': re.compile(r'\bFOR\s+[A-Za-z][\w$#]*\s+IN\s*\(\s*SELECT\b', re.I),
    'SEC001': re.compile(r'\bEXECUTE\s+IMMEDIATE\b|\bDBMS_SQL\s*\.\s*PARSE\b', re.I),
    'SEC002': re.compile(r'\bWHEN\s+OTHERS\s+THEN\b', re.I),
    'SQL003': re.compile(r'\bCOMMIT\s*;', re.I),
}


def analyze_sql(source: str, path: str = '<input>', disabled: set[str] | None = None) -> list[Finding]:
    disabled = disabled or set()
    masked = mask_sql(source)
    findings = []
    for rule, pattern in PATTERNS.items():
        if rule in disabled:
            continue
        severity, message, suggestion = RULES[rule]
        for match in pattern.finditer(masked):
            line = source.count('\n', 0, match.start()) + 1
            # Allow a narrow, auditable per-line suppression: -- devkit: ignore SQL001
            original_line = source.splitlines()[line - 1]
            if re.search(r'--\s*devkit:\s*ignore\s+' + rule + r'\b', original_line, re.I):
                continue
            findings.append(Finding(rule, severity, path, line, message, suggestion))
    return sorted(findings, key=lambda f: (f.path, f.line, f.rule))
