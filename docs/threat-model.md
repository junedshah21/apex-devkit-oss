# Threat model

**Assets:** proprietary application exports, credentials that might appear in them, workstation data, report outputs, developer trust.

**Threats:** malicious ZIP paths/compression bombs; extremely large exports; deceptive commented-out syntax; secrets copied into public issue reports; unauthorized schema reads; false assurance from heuristic findings.

**Controls in v0.1:** no eval/SQL execution or network calls, only `.sql` ZIP members processed, traversal and size/member checks, limited local scanner, no database connection from CLI. Metadata script uses `USER_*` only and is read-only.

**Residual risk:** ZIP can consume memory before decompression; symlinked directories inside inspected directory need further containment; Oracle nested syntax can create false findings; secret values can flow into user-selected reports. Run on trusted local files, ideally in a sandbox, and review reports before sharing. Untrusted external export uploads are NOT a supported service use case.

Please disclose suspected vulnerabilities privately using SECURITY.md, not public issues containing customer data.
