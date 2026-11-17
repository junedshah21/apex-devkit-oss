# Real APEX export validation — pending content inspection

Date: 2026-11-17

The repository contains `tests/fixtures/apex-exports/f199526.sql` (Git blob `d9068140cd754aa7c90cada369256d0b5bd3c059`, 11,343,735 bytes), uploaded via commit `0fcf9fae0c10903c55130075e45cf65caae9ae36`. GitHub repository API metadata confirms the upload, **but the GitHub integration rejected raw content retrieval because of size**. Therefore:

- **NOT RUN:** actual export inspection of `f199526.sql`;
- **NOT VERIFIED:** application ID, APEX version, pages/components, credentials/security posture, ownership or redistribution permissions;
- **NOT CLAIMED:** compatibility with a genuine Oracle APEX export;
- **PASS:** existing local synthetic unit/regression suite, 17/17 tests via `sh scripts/check.sh` on 2026-11-17 (Python 3.13.5).

## Next safe QA step

1. Verify the uploaded APEX application is personally owned or properly licensed for public redistribution. If not, remove the file and consider repository history cleanup.
2. Check export contents locally for hardcoded passwords, keys, tokens, internal URLs, customer identifiers, proprietary logic and data. **A public repository preserves history; deleting the file from HEAD alone is not enough to remove secrets from old commits.** Rotate any exposed secrets and follow GitHub's sensitive-data removal guidance.
3. To validate the export without publishing more data, obtain the authorized, sanitized file in a test environment and execute `apex-devkit inspect-export f199526.sql --format json --output export-report.json`. Review the report before sharing. Do not execute import scripts.
4. Compare counts with an authorized APEX application export and add only minimal synthetic or explicitly redistributable regression fixtures.
5. Keep GitHub release and OpenAI application submission on hold pending evidence.

The current file is smaller than the CLI's 20 MiB SQL input cap, but that fact alone does **not** establish successful processing.
