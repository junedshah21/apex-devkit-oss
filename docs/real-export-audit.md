# Verified real APEX export static review — 2026-11-17

Repository file: `tests/fixtures/apex-exports/f199526.sql`; Git blob `d9068140cd754aa7c90cada369256d0b5bd3c059` (11,343,735 bytes). Parts `f199526_part01.txt` through `f199526_part08.txt` are readable. Concatenating all 8 and converting CRLF to LF yields **exact content equality** with the original Git blob (53,141 lines including the final empty line). No missing or reordered content was detected.

## Export metadata and counts

| Item | Observed |
|---|---:|
| Application ID | 199526 |
| APEX flow version string in export | 24.2.0 |
| APEX release string in export | 26.2.1 |
| Page declarations | 18 |
| Page region declarations | 51 |
| Report region declarations | 3 |
| All region declarations | 54 |
| Page item declarations | 22 |
| Page button declarations | 28 |
| Dynamic action events | 14 |
| Dynamic action actions | 28 |
| Page process declarations | 17 |
| Authentication scheme declarations | 1 |
| Authorization scheme declarations recognized by targeted signature scan | 0 |
| Application static file declarations | 82 |

The top-of-file export summary includes 18 pages, 54 regions, 17 processes and 14 dynamic actions; these match signature counts once report regions are counted separately. Export contains a terminal `...done` marker, not proof of successful import.

## Security/privacy interpretation

- **Do not infer vulnerabilities** from a missing authorization-scheme declaration alone. Review all public pages, page processes, component conditions and authorization rules in an authorized APEX environment.
- A targeted source pattern review identified no obvious private-key headers or AWS access-key ID signatures. This is **not** complete credential scanning and does not prove that application logic or metadata is safe for public release.
- This SQL export includes exporter identity metadata (including an email address) and application configuration; publication was made by the repository owner before this review. Confirm that the export is the user's own redistributable demo and deliberately safe to publish. If not, remove the asset and consult GitHub history cleanup guidance; file deletion alone does not erase Git history.
- Application export contents, static files and third-party components must have redistribution rights before permanently distributing them as an MIT project fixture.

## Validation performed and not performed

- **PASSED:** GitHub byte-content equality after CRLF normalization and component signature/header reconciliation; reconstructed source was scanned in memory using targeted JavaScript expressions.
- **PASSED:** Local Python toolkit regression suite 18/18 on synthetic fixtures after adding `create_report_region` recognition.
- **NOT EXECUTED:** The published Python CLI directly on the reconstructed 11.3 MB SQL, due to the GitHub connector's separate execution environment. The read-only analysis above is an independent structural scan.
- **NOT EXECUTED:** Live Oracle APEX installation, app runtime checks, SQLcl database access, exploitation testing, full code or secret audit.

No OpenAI application was submitted and this note does not claim verified Oracle runtime compatibility.
