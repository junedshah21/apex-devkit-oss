# Release policy and checklist

Semantic versions: 0.x for experimental APIs, minor increases for new capabilities, patch for compatible fixes. The first public release is permitted **only** after repository creation, safe-code and dependency review, reproducible tests, and explicit review of public content. Publish a Git tag and release notes from the exact tested commit; do not call an untagged draft a release.

Local validation (GitHub Actions unnecessary): `./scripts/check.sh`. Recommended release gate for later versions: verify source fixtures with authorized Oracle APEX 24.x exports, verify package install on multiple Python versions, verify ZIP hardening, review all third-party licenses, and scan repository history for secrets.

No automation performs cloud/database writes; optional SQL scripts require an explicitly authorized session.
