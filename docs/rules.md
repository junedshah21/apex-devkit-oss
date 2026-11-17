# Advisory rule catalog

These are **lexical** signals, not proven defects. Confidence is `low`; severity indicates suggested review priority.

| ID | Severity | Trigger | Common false positive |
|---|---|---|---|
| SQL001 | medium | `SELECT * FROM` | Deliberate ad hoc queries |
| SQL002 | low | `FOR x IN (SELECT` | Small result sets, well-tuned loops |
| SEC001 | medium | `EXECUTE IMMEDIATE` or `DBMS_SQL.PARSE` | Safely bound and validated SQL |
| SEC002 | medium | `WHEN OTHERS THEN` | Correct business-specific fallback/re-raise |
| SQL003 | low | `COMMIT;` | Standalone transaction owner |
| APEX001 | low | `p_authentication_id=>null` | Partial export or version-specific defaults |

Suppress inline with `-- devkit: ignore SQL001` on the matching line, or globally with `--disable SQL001` on `lint`. Report findings can contain source paths. Never treat the absence of a finding as proof of safety.
