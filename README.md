# APEX DevKit OSS

**Experimental v0.1.0 candidate — not Oracle-certified.** Small, independent MIT-licensed toolkit for **offline, read-only** review of Oracle APEX exports and SQL/PLSQL source.

## Current functionality

- `lint`: conservative lexical advisories for `SELECT *`, cursor loops, dynamic SQL, `WHEN OTHERS`, and `COMMIT`.
- `inspect-export`: counts recognized APEX SQL export component declaration signatures in a single `.sql`, split folder, or ZIP. Reviews one authentication declaration pattern.
- Outputs JSON or Markdown. `--disable SQL001` and inline `-- devkit: ignore SQL001` suppress an advisory.
- `sql/schema_inventory.sql`: **optional**, manually executed read-only Oracle user-schema metadata queries. Not integrated into the Python CLI.
- `examples/apex_ajax_callback.sql`: original sample, **not** an installed APEX application.
- [`examples/synthetic_apex_export.sql`](examples/synthetic_apex_export.sql): self-authored, illustrative declaration fixture (not an installable application); [reproducible demo](docs/use-case-demo.md).

These utilities are not a full Oracle SQL parser, vulnerability scanner, or a certified APEX application analyzer. No SQL or APEX export is executed by the Python tools. Treat findings as prompts for human review. The export file might contain secrets; **never publish sensitive export files or their reports without review**.

## Requirements and quick start

Python 3.10+; no runtime Python dependencies and **no database connection** for the CLI.

```sh
python -m venv .venv
. .venv/bin/activate             # Windows: .venv\Scripts\activate
python -m pip install -e .
apex-devkit lint path/to/sample.sql --format markdown
apex-devkit inspect-export path/to/f123.sql --format json --output report.json
apex-devkit inspect-export path/to/f123/ --format markdown
./scripts/check.sh              # Windows: PYTHONPATH=src python -m unittest discover -s tests -v
```

An alternative without installing: `PYTHONPATH=src python -m apex_devkit lint example.sql`.

## Verification and responsible fixtures

- Historical verification: Python 3.13.5 reconstructed-source tests **23/23 passed**, with an editable-install and synthetic CLI smoke check. This is not a byte-identical Git checkout validation or an Oracle runtime claim. See [QA report](docs/qa-report.md).
- A previously uploaded real APEX export and its eight fragments were **removed from the current public main branch** because ownership and redistribution clearance could not be established. Historic Git revisions may still expose these artifacts. If sensitive data was included, follow a separate GitHub history and credential incident response.
- The public demonstration uses only self-authored synthetic fixtures; no genuine APEX application installation is claimed.

## Safety and input limits

ZIP archives: no extraction to disk, no traversal paths, maximum 1,000 entries and 20 MiB total declared uncompressed size. SQL input: 20 MiB. Use trusted exports only. The tool does not execute them. Common Oracle alternative quoting (`q'[...]'` etc.) is masked, but this is not a complete Oracle parser; newer APEX component families may be unrecognized. ZIP compression-bomb protection and resource limits require further hardening before processing untrusted public uploads.

## Maintenance

- [Architecture, limits, and permissions](docs/architecture.md)
- [Rule guide](docs/rules.md)
- [Threat model](docs/threat-model.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md) and [Security policy](SECURITY.md)
- [Quality report](docs/qa-report.md)
- [Release process](docs/release-process.md)

## Disclaimers

This independent project is not affiliated with or endorsed by Oracle or OpenAI. Oracle and APEX are trademarks of their respective owners. The current main branch uses self-authored public examples and no longer contains the previously published real APEX export fixture. Historical Git commits may still contain that export; ownership and redistribution rights for that historical material have not been verified. Do not interpret removal from main as Git history sanitization. This repository has no dependency on GitHub Actions.
