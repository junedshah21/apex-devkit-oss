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

## Reconstructed-source regression execution (2026-11-17)

The GitHub connector supplied the Python module text and two test files from draft PR #2. Because direct `git clone` failed with DNS resolution error, a fresh local Python 3.13.5 environment was populated manually from these retrieved source listings and the following command executed:

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
```

**Result:** 23 tests run; 23 passed; 0 failures; 0 errors. Tests covered rule masking/suppressions, component signature detection, SQL/ZIP/directory equivalence, UTF-8 BOM exact byte accounting, security rejection cases, CLI JSON and large multiline diagnostic offsets.

**Scope qualification:** This is a real Python execution of reconstructed code matching the retrieved implementation in behavior, not proof of running the exact Git checkout or installable package. Source was manually reconstituted, rather than independently checked byte-for-byte against repository blob SHA; exact checkout/package-install validation and Python version matrix remain outstanding. Genuine full `f199526.sql` CLI analysis, Oracle APEX runtime tests and public fixture ownership/privacy clearance also remain outstanding.

## Reconstructed-source packaging smoke test (2026-11-17)

Python 3.13.5, in the same manually reconstructed local project tree, successfully executed `python -m pip install --no-build-isolation --no-deps -e .`. The installed `apex-devkit inspect-export examples/synthetic_apex_export.sql --format json` completed successfully and recognized **8 component types**, each with count **1**, from the self-authored illustrative example. Because the checkout was reconstructed manually, this is **not** byte-for-byte independently verified Git checkout testing; it does not validate the untested Python 3.10-3.12 versions or Oracle runtime.
