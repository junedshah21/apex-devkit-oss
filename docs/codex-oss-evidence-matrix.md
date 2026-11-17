# Codex for Open Source — requirement-to-evidence matrix

Reviewed: 2026-11-17. Evidence-backed preparation only; this is **not** a submitted application or a promise of acceptance.

Sources:
- https://openai.com/form/codex-for-oss/
- https://developers.openai.com/community/codex-for-oss

The public guidance says maintainers of active open-source projects may apply. Review signals include meaningful usage, broad adoption **or clear importance to the ecosystem**, alongside repository usage and evidence of active maintenance (PR reviews, issue triage, releases). There is no published fixed minimum star count, download count or project age. The application is reviewed on a rolling basis. Selection is discretionary.

| Official criterion / form field | Current verifiable evidence | Assessment / next step |
|---|---|---|
| Public repository and GitHub username | Public repo `junedshah21/apex-devkit-oss` | Present; confirm GitHub user profile is public |
| Primary/core maintainer role | Repo owner has admin/write access, contributions, PRs | Present; describe concrete ongoing responsibilities, no inflated team claims |
| Meaningful usage / adoption or ecosystem importance | Independent offline, read-only APEX export inspection and SQL linting tool with sample | Real adoption unproven; justify niche workflow through actual tests and independent feedback, not fabricated download/user counts |
| Evidence of active maintenance | Commits, PR #1 merged, PR #2 open as draft, issue #3 | Present but very recent; maintain review/triage and publish verified release history |
| Release management | v0.1.0 code candidate; no published release | Blocked: testing and public fixture safety |
| Security and code-quality responsibilities | Tests, bounds, threat model, no database writes | Incomplete: run full tests, check ZIP edge cases and review public export permission/sensitive data |
| Why this repo qualifies (max 500 characters) | Value proposition and truthful maintainership evidence | Draft carefully, note early stage; do not invent stars/downloads/users |
| ChatGPT-account email / applicant names | Not stored in repository | User enters privately, use exact current account details |
| OpenAI Organization ID | Not in repository | User retrieves securely from OpenAI Platform; never commit publicly |
| API-credit use (max 500 characters) | Possible optional, consent-based PR triage / explainability workflows | State future plans, not implemented capabilities |
| Optional information (max 500 characters) | Real test/release evidence once complete | Update before submission |
| Terms and redemption | Official program terms linked from form; six-month Pro is for selected maintainers | Applicant reviews terms; separately verify promo redemption eligibility with active subscription before changing it |

## Evidence gates before recommending submission

- [ ] Review and clear public `f199526.sql` plus all fragments, embedded assets, and repository history for ownership, redistribution rights, and sensitive data. If uncertain, remediate disclosure; deletion from HEAD alone does not scrub git history.
- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests -v` in a trusted full checkout. Record Python version, actual test count and full result.
- [ ] Execute CLI on an authorized, sanitized real APEX export and compare against independently observed declarations. Never execute exported SQL for this check.
- [ ] Package/install test on the declared Python versions and inspect ZIP input limits; document only proven support.
- [ ] Review source, licenses, and security documentation, then publish a release based on the exact tested commit.
- [ ] Gather authentic issue reports, third-party usage feedback or other credible ecosystem evidence; avoid artificial stars, downloads, PRs, or testimonials.
- [ ] Recheck the official form and terms at the time of submission, verify identity/email/Organization ID privately and final 500-character limits.

## Submission decision

**Not ready to recommend submission** until the specific QA, public-content and credibility gaps above are addressed or explicitly assessed. This is an internal release-readiness judgment, not a claim about OpenAI's decision, which remains independent. The applicant controls final submission.
