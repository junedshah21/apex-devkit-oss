# QA execution report — 2026-11-17

Environment: Python 3.13.5, Linux container; local project source. No Oracle Database or live APEX environment was used.

| Validation | Status |
|---|---|
| Python compilation | PASS |
| Unit and regression tests with `PYTHONPATH=src` | PASS: 17 tests, 0 failures |
| CLI tests within suite | PASS |
| Synthetic ZIP traversal, size and symlink regression tests | PASS |
| Runtime Python dependencies | None declared |
| Live Oracle schema inventory | NOT RUN |
| Real sanitized APEX export fixtures | NOT RUN |
| Multi-version Python compatibility | NOT RUN |
| Full independent security/license audit | NOT RUN |
| Authentic public adoption | NOT ESTABLISHED |

Direct `python -m unittest discover -s tests -v` **without installation or PYTHONPATH** produced ModuleNotFoundError, as expected for a src-layout project. The bundled `scripts/check.sh` sets PYTHONPATH correctly and passes. Source inspection and targeted secret-pattern scanning do not replace independent security review. No formal release tag is claimed.
