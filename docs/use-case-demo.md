# Reproducible offline APEX export demonstration

This self-authored minimal example demonstrates the **scope and limitations** of the APEX DevKit OSS inspector without publishing any customer or employer export.

## Run locally

Install Python 3.10+ and clone the repository in a trusted environment. No Oracle database, network access, GitHub Actions, or credentials are required for the CLI.

```sh
python -m pip install -e .
apex-devkit inspect-export examples/synthetic_apex_export.sql --format json
apex-devkit lint examples/synthetic_apex_export.sql --format markdown
```

Without installation on macOS/Linux, use `PYTHONPATH=src python -m apex_devkit inspect-export examples/synthetic_apex_export.sql --format json`. On Windows PowerShell, run `$env:PYTHONPATH="src"; python -m apex_devkit inspect-export examples/synthetic_apex_export.sql --format json`.

## Expected interpretation

The inspector should identify one each of: `pages`, `regions`, `report_regions`, `page_items`, `buttons`, `dynamic_actions`, `page_processes`, and `shared_lovs`. These are signature counts, not evidence that Oracle APEX would successfully import this illustrative file. The lint command may produce no advisories; that is **not** security clearance.

## Responsible use

- Inspect only software and exports you own or have permission to review.
- Never publish real exports with customer data, hard-coded credentials, secrets, non-public URLs, identities, or third-party proprietary assets.
- For real authorized APEX exports, compare tool output with App Builder details and review discrepancies manually. New APEX versions may introduce component families the inspector does not recognize.
- Report reproducible bugs using a newly written minimal synthetic sample. Do not attach sensitive real exports to public GitHub issues.

This demo makes no claims about download numbers, external adopters, Oracle certification, or a production runtime test.
