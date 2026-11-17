# APEX DevKit OSS

Independent MIT-licensed, offline and read-only advisory toolkit for Oracle APEX developers. **Experimental v0.1.0 source snapshot, not Oracle-certified.**

The project provides conservative SQL/PLSQL static advisories and read-only APEX export inspection for SQL files, split export folders, and ZIPs. It is not a full parser, a vulnerability scanner, or a substitute for professional security review. No input SQL is executed.

**Development:** Python 3.10+; no runtime third-party dependencies. After installing with `python -m pip install -e .`, run `apex-devkit lint sample.sql --format markdown` or `apex-devkit inspect-export f100.sql --format json`. Run local QA via `./scripts/check.sh`. No GitHub Actions dependency.

See [architecture](docs/architecture.md), [rules](docs/rules.md), [QA](docs/qa-report.md), [security policy](SECURITY.md), and [roadmap](ROADMAP.md).

This project is not affiliated with Oracle or OpenAI. Real Oracle compatibility and public adoption have not been established. Do not publish confidential exports or reports.
