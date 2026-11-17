# Codex for Open Source — reviewed draft, NOT SUBMITTED

Official form: https://openai.com/form/codex-for-oss/

- GitHub username: `junedshah21`
- Repo URL: https://github.com/junedshah21/apex-devkit-oss
- Maintainer role: **Primary maintainer** (repository administrator; verify individual contributions before finalizing)
- First name, last name, and **ChatGPT account email**: applicant fills privately.
- **OpenAI Organization ID**: applicant retrieves privately from https://platform.openai.com/settings/organization/general; do not commit it.
- Interest in Codex Security/API credits: applicant selects based on their actual intended use. Credits are optional/discretionary.
- 6-month Pro remains subject to OpenAI selection and redemption eligibility.

## Why does this repository qualify? (466/500 characters)

APEX DevKit OSS is a free, MIT-licensed, offline Python toolkit for Oracle APEX developers. It provides read-only export component inspection and conservative SQL/PLSQL linting with reproducible examples and tests. As the repository's primary maintainer, I implement fixes, review PRs, triage issues, and maintain its docs. The project is early-stage with no verified external adoption yet; it addresses a niche APEX workflow and documents limitations transparently.

## How will you use API credits? (365/500 characters)

I would use API credits to prototype opt-in explanations for static SQL/APEX findings, summarize user-submitted issues and PRs, and improve test-case generation and maintainer documentation. Any code submitted for AI analysis would require the contributor's permission and privacy review. The offline CLI would remain usable without an API key or external services.

## Anything else? (411/500 characters)

The public repository contains original synthetic examples, a Python CLI, regression tests, a threat model, and issue/PR history. The project was created in November 2026 and is experimental. I make no claims of Oracle certification, significant downloads, or established community adoption. A real APEX export's redistribution review remains open, and the application will be updated to reflect its resolution.

## Unresolved before final recommendation

1. The owner must confirm whether the previously published `f199526.sql` and eight fragments are owned and redistributable; no such confirmation was found. Draft PR #4 proposes removal from public HEAD while retaining self-authored synthetic tests, but **is not merged**. Removal does not purge Git history.
2. The tested reconstructed-source suite (23 passes) and CLI smoke test do not prove actual Oracle runtime compatibility or a byte-identical Git checkout QA run.
3. Genuine ecosystem impact/third-party adoption has not yet been established. No fake metrics should be supplied.
4. Verify the official terms and email/account redemption requirements before submitting; the applicant must authorize and submit the actual form.

Prepared for review, not for automated submission.
