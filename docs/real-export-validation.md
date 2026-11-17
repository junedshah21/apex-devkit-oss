# Real APEX export validation — consolidated status (2026-11-17)

This document supersedes the earlier *pending content inspection* note. The evidence and detailed static counts are in [real-export-audit.md](real-export-audit.md).

## Verified from published Git objects

- `f199526.sql` is present at `tests/fixtures/apex-exports/f199526.sql`, with Git blob `d9068140cd754aa7c90cada369256d0b5bd3c059` (11,343,735 bytes).
- All eight `f199526_part01.txt`–`part08.txt` files are readable. Ordered concatenation with CRLF-to-LF normalization matched the original Git blob; the reconstructed source has 53,141 lines including the final empty line.
- An independent structural signature scan confirmed 18 page declarations, 54 region declarations including 3 report-region declarations, 22 page items, 28 buttons, 14 dynamic-action events and 17 page processes.
- A follow-up change added `create_report_region` signature recognition. The prior reported local synthetic regression result was **18/18 passed**; the older [QA report](qa-report.md) records its earlier 17/17 result.

## Not verified — release blockers

- **NOT RUN:** executing the Python CLI on the full authentic 11.3 MB export inside the same test environment. Git blob reconstruction and a separate structural scan are not equivalent to CLI execution.
- **NOT RUN:** installation/import into a live authorized Oracle APEX instance, runtime or DB permission testing, independent full source/dependency/license/security audit.
- **NOT ESTABLISHED:** ownership, full sanitization, redistribution rights or safety of the published fixture. Exporter identity metadata and application configuration are included in the public file. A limited secret-pattern scan is not comprehensive.

## Required next steps

1. Review whether the complete fixture and all embedded static assets are self-owned and approved for public redistribution. If rights or data safety are uncertain, remove public access and follow GitHub's sensitive-data history-removal procedures; deleting a file from the latest commit does not remove its history. Rotate any exposed secrets.
2. Use an authorized, sanitized copy in a controlled test environment to run `apex-devkit inspect-export path/to/f199526.sql --format json` and compare the output with the independently observed signatures. Do not execute the export SQL.
3. Add regression tests for the recognized export signatures using newly written synthetic fixtures without embedding potentially sensitive application code.
4. Validate package installation on supported Python versions, ZIP safety limits and licensing before an official tagged release.
5. Keep any claims of Oracle certification, runtime compatibility, full security clearance, and external program eligibility on hold until independently established.

No GitHub release or external application is claimed or authorized by this update.
