# Codex for Open Source — reviewed draft, NOT SUBMITTED

Official form: https://openai.com/form/codex-for-oss/

- GitHub username: `junedshah21`
- Repo URL: https://github.com/junedshah21/apex-devkit-oss
- Maintainer role: **Primary maintainer** (repository administrator; verify individual contributions before finalizing)
- First name, last name, and **ChatGPT account email**: applicant fills privately.
- **OpenAI Organization ID**: applicant retrieves privately from https://platform.openai.com/settings/organization/general; do not commit it.
- Interest in Codex Security/API credits: applicant selects based on their actual intended use. Credits are optional/discretionary.
- 6-month Pro remains subject to OpenAI selection and redemption eligibility.

## Why does this repository qualify? (472/500 characters)

APEX DevKit OSS is a free, MIT-licensed, offline Python toolkit for Oracle APEX developers. It provides read-only export component inspection and conservative SQL/PLSQL linting with reproducible examples and tests. As repository owner and primary maintainer, I oversee development, review and merge changes, maintain documentation, and track issues. The project is new and has no verified external adoption yet, but addresses a niche APEX workflow with transparent limits.

## How will you use API credits? (365/500 characters)

I would use API credits to prototype opt-in explanations for static SQL/APEX findings, summarize user-submitted issues and PRs, and improve test-case generation and maintainer documentation. Any code submitted for AI analysis would require the contributor's permission and privacy review. The offline CLI would remain usable without an API key or external services.

## Anything else? (492/500 characters)

This is an early-stage, independently maintained Python CLI with self-authored synthetic fixtures and documented QA limitations. Its goal is to give Oracle APEX developers a transparent, offline way to inspect export structure and review basic SQL patterns. The previously public real-export fixture was removed from current main pending redistribution review; historical Git commits may still contain it. I do not claim third-party adoption, Oracle certification, or a production deployment.

## Unresolved before final recommendation

1. The owner must confirm whether the previously published `f199526.sql` and eight fragments are owned and redistributable; no such confirmation was found. PR #4 has been **merged** to remove the original export and fragments from the current public HEAD, while retaining synthetic tests. Removal does not purge Git history.
2. The tested reconstructed-source suite (23 passes) and CLI smoke test do not prove actual Oracle runtime compatibility or a byte-identical Git checkout QA run.
3. Genuine ecosystem impact/third-party adoption has not yet been established. No fake metrics should be supplied.
4. Verify the official terms and email/account redemption requirements before submitting; the applicant must authorize and submit the actual form.

Prepared for review, not for automated submission.
