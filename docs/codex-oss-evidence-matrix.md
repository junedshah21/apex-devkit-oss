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
| Evidence of active maintenance | Commits, PRs #1, #2 and #4 merged; issue #3 | Present but very recent; maintain review/triage and publish verified release history |
| Release management | v0.1.0 code candidate; no published release | Still unreleased; synthetic reconstructed-source QA passed (23/23), live Oracle and exact Git checkout tests not verified |
| Security and code-quality responsibilities | Tests, bounds, threat model, no database writes | Incomplete: run full tests, check ZIP edge cases and review public export permission/sensitive data |
| Why this repo qualifies (max 500 characters) | Value proposition and truthful maintainership evidence | Draft carefully, note early stage; do not invent stars/downloads/users |
| ChatGPT-account email / applicant names | Not stored in repository | User enters privately, use exact current account details |
| OpenAI Organization ID | Not in repository | User retrieves securely from OpenAI Platform; never commit publicly |
| API-credit use (max 500 characters) | Possible optional, consent-based PR triage / explainability workflows | State future plans, not implemented capabilities |
| Optional information (max 500 characters) | Real test/release evidence once complete | Update before submission |
| Terms and redemption | Official program terms linked from form; six-month Pro is for selected maintainers | Applicant reviews terms; separately verify promo redemption eligibility with active subscription before changing it |

## Final official terms review (checked 2026-11-17)

Official terms: https://developers.openai.com/codex/codex-for-oss-terms

- OpenAI requires accurate, complete applicant/repository/maintainer information and may verify repository control.
- It may approve or deny applications at its discretion; capacity and ecosystem significance are review factors.
- Misleading information, multiple identities, unauthorized testing or legal/security risk can lead to rejection or revocation.
- Program availability and benefits can change or end; avoid claiming guaranteed duration or activation on a specific existing subscription.
- Do not submit confidential information in the application.
- Official application remains open with rolling reviews and no published fixed close date at the time of this check.

**Remaining disclosure risk:** PR #4 removed the real `f199526.sql` and its eight parts from current public `main`, but historical Git objects can still expose the content. Ownership and redistribution rights remain unverified. PR #2 has merged, with 23/23 tests passed on manually reconstructed Python 3.13.5 source, not on a byte-verified Git clone. Exact checkout and Oracle runtime remain unverified.

## Deadline and prioritization (official page checked 2026-11-17)

The live [application form](https://openai.com/form/codex-for-oss/) explicitly says applications are reviewed **on a rolling basis**. **No fixed closure date is published on that page.** This does not guarantee the offer will remain available. Therefore do not postpone submission indefinitely waiting for vanity metrics or an arbitrary repository age.

Prioritize critical gates: repository ownership, privacy/redistribution permission, honest functioning demo, reproducible tests, and accurate application answers. Legitimate adoption evidence should be collected as it occurs; do not buy or fake stars, downloads, endorsements or activity. The applicant makes the final submission decision after reviewing the official terms.

## Evidence gates before recommending submission

- [ ] Confirm historical `f199526.sql` and embedded assets' ownership, redistribution rights and potential sensitivity. PR #4 removed them from HEAD, not Git history; investigate history remediation if required.
- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests -v` in a byte-verified full Git checkout. Historical reconstructed-source Python 3.13.5: 23/23 passing, documented separately.
- [ ] Execute CLI on an authorized, sanitized real APEX export and compare against independently observed declarations. Never execute exported SQL for this check.
- [ ] Package/install test on the declared Python versions and inspect ZIP input limits; document only proven support.
- [ ] Review source, licenses, and security documentation, then publish a release based on the exact tested commit.
- [ ] Gather authentic issue reports, third-party usage feedback or other credible ecosystem evidence; avoid artificial stars, downloads, PRs, or testimonials.
- [ ] Recheck the official form and terms at the time of submission, verify identity/email/Organization ID privately and final 500-character limits.

## Submission decision

**Not ready to recommend submission** until the specific QA, public-content and credibility gaps above are addressed or explicitly assessed. This is an internal release-readiness judgment, not a claim about OpenAI's decision, which remains independent. The applicant controls final submission.
