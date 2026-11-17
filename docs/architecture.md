# Architecture and compatibility

## Boundaries

`src/apex_devkit/analysis.py`: lightweight offset-preserving masking of common SQL comments/literals, lexical rule matching. `exports.py`: read-only component-signature counting in SQL, ZIP and folders. `cli.py`: output formatting and controlled CLI errors. All file processing runs locally with Python standard library. Schema inventory is separate SQLcl script under `sql/`.

## Permissions

| Feature | Privilege | Requirement |
|---|---|---|
| Python lint/inspect | Local read access to input | No Oracle login; no DBA rights |
| Schema inventory | Authorized Oracle session, own schema dictionary views (`USER_*`) | Database account required; no DBA role needed for own metadata |
| APEX AJAX example | Permission to edit an APEX application and execute APEX_JSON | APEX workspace access; application authorization still required |

## Compatibility claims

| Target | Current status |
|---|---|
| Python 3.10+ | Tested only on environment recorded in QA report |
| APEX 24.1/24.2 single SQL export signatures | Design target; synthetic fixtures only; real export unverified |
| APEX 24.2 split SQL folder / ZIP | Design target; synthetic fixture coverage; real export unverified |
| APEX 26.x | Not verified; export format subject to change |
| Oracle Database 19c, 21c, 23ai/26ai | SQL inventory not executed against live DB; no claim |
| ORDS | No integration in this release |

Oracle APEX 24.2 export documentation: https://docs.oracle.com/en/database/oracle/apex/24.2/aeadm/exporting-one-or-more-applications.html

## Installation / upgrades / removal

`python -m pip install -e .` installs the CLI into an isolated environment. Upgrade using a new tagged source checkout and reinstall. Remove with `python -m pip uninstall apex-devkit-oss`. CLI creates no database objects, and no migration/uninstall SQL is needed. Run the optional schema inventory only against schemas you are authorized to inspect. Never commit source exports that contain secrets.

## Future modules (not implemented)

A grammar-based Oracle parser, component-specific APEX authorization reviews, measured performance diagnostics, PK/FK schema Markdown/diagram generator, and broad APEX example catalog are future milestones. For explain plans, use `DBMS_XPLAN` only when authorized and only with appropriate performance/cost awareness. No automatic index modification is planned.
