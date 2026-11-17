# Codex for Open Source — evidence-based application preparation

Updated: 2026-11-17. Official form: https://openai.com/form/codex-for-oss/

This is a **draft, not a submitted application**. Approval and redemption of six months of ChatGPT Pro are at OpenAI's discretion, and publishing a new repository does not itself demonstrate adoption.

## Verified project evidence

- Repository: https://github.com/junedshah21/apex-devkit-oss
- Public repository, created 2026-11-17; maintainer has repository write/admin access.
- At preparation time GitHub reported **0 stars and 0 forks**; no user/download figures have been established.
- Independent MIT-licensed Python 3.10+ offline and read-only static advisory toolkit for Oracle APEX export and SQL review; does not run SQL or connect to a database.
- A previously published 11.3 MB real APEX export was reconstructed from 8 parts and statically inspected; historical details are in [real-export-audit.md](real-export-audit.md). The export and fragments have since been excluded from current `main` via PR #4 because rights were unverified. Git history may still contain them.
- Historical tests: 17/17, then 18/18; after the PR #2 changes, 23/23 tests passed on a manually reconstructed Python 3.13.5 source checkout, plus editable install and demo CLI smoke test. The exact Git checkout and real export CLI execution were not verified; **live Oracle runtime** was not tested.
- GitHub Actions is not required. Formal release, adoption evidence, independent security and permission checks remain outstanding.

## Official application inputs — prepare accurately

The form asks for first name, last name, ChatGPT-account email, public GitHub username, public repository URL, primary/core maintainer role, why the repository qualifies (500 characters), interest in Codex Security and/or API credits, OpenAI Organization ID, API-credit use (500 characters), and optional other information (500 characters). The applicant must provide and verify their own email and Organization ID; do not put these sensitive identifiers in the public repository.

### Draft: Why does this repository qualify? (under 500 characters)

APEX DevKit OSS is an independent, offline Python toolkit for reviewing Oracle APEX exports and SQL/PLSQL with conservative, explainable findings. It targets a developer workflow where export inspection can be cumbersome, and keeps analysis read-only. I maintain the code, tests, documentation, and security limits. This is an early-stage project; I do not claim significant adoption yet. I aim to improve real-export coverage and build a reliable community tool.

### Draft: How will you use API credits? (under 500 characters)

If awarded API credits, I would prototype opt-in explanations of SQL/APEX static-review findings, draft maintainer triage summaries, and assist with pull-request review and tests. All workflows would be scoped to code the contributor has rights to share, with explicit consent and redaction; sensitive APEX exports would not be sent to an external service by default. I would measure usefulness and costs before enabling any hosted workflow.

### Draft: Anything else? (under 500 characters)

I am the primary maintainer of this newly published project. The toolkit is experimental, with documented limits, regression tests, and an ongoing real-export verification effort. I am seeking maintainer support to strengthen parser accuracy, release quality, security checks, and documentation. I understand that the project has not demonstrated broad adoption or Oracle-certified compatibility.

## Recommended evidence milestones before submitting

1. Establish the historical real APEX export's ownership and redistribution rights, including embedded assets; PR #4 removed the files from HEAD, but historical copies may remain and require separate remediation if sensitive. A Git commit deletion does not scrub historical copies.
2. Complete full genuine-export CLI tests in a controlled local environment and independently document expected results.
3. Add original synthetic regression fixtures, improve ZIP decompression protections, and run a documented Python version matrix.
4. Complete a reviewed versioned release with exact tested commit and release notes.
5. Build **real** usage evidence through reproducible examples, issue responses, technical discussions or verified user feedback. Never fabricate adoption or reviews.
6. Verify the official form and program terms immediately before applying. The user must supply their ChatGPT email and OpenAI Organization ID privately and review the final application.

## Submission and redemption

Do not claim an application has been filed without submission confirmation. OpenAI selects applicants on a rolling basis, so a legitimate application can still be declined. Acceptance also does not by itself verify successful redemption on a particular existing subscription; check the specific terms and any redemption issue with the program/support before making subscription changes.
