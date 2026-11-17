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

## Follow-up work pending full execution (2026-11-17)

Draft PR #2 adds a self-authored synthetic APEX sample, SQL/ZIP/directory/CLI regression coverage, UTF-8 BOM byte-budget tests, and SQL linting line-number/performance updates. The newest PR #2 suite **has not been executed in a complete checkout** in the available environment because the container cannot resolve GitHub. Earlier 17/17 and 18/18 results predate this PR and must not be presented as results for the current branch. Targeted standalone byte-budget and line-offset assertions are not substitutes for the full suite.

Run this reproducibly from a trusted repository checkout without GitHub Actions:

```sh
python --version
python -m pip install -e .
python -m unittest discover -s tests -v
apex-devkit inspect-export examples/synthetic_apex_export.sql --format json
```

Record actual test counts, environment and CLI output only *after* running them; do not backfill expected pass numbers. The real `f199526.sql` artifact is public, but full disclosure/redistribution review is not complete. Do not claim full security clearance, production Oracle compatibility, or formal release readiness from these synthetic checks.
