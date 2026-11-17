# Sanitized Oracle APEX application export fixtures

Upload **only self-owned, synthetic or fully sanitized test application exports** here as `.sql` files.

This directory is in a PUBLIC GitHub repository. Do not upload employer/client code, real usernames, customer records, credentials, API keys, authentication secrets, internal URLs, or sensitive configuration. Oracle APEX export scripts can contain embedded settings, SQL, static files, and application logic. Review exports before committing.

Recommended file names: `demo_apex_24_2.sql` or `sample_app_f100.sql`.

Each fixture should include a separate short note recording APEX version, export mode (single SQL or split), whether it is sanitized, and whether it may be redistributed under MIT. Never claim successful live Oracle validation from static inspection alone.

The Python inspector reads exported SQL as data and does not run it. Uploading here does NOT import SQL into Oracle APEX.

If you cannot verify that the export is safe for public disclosure, do NOT upload it here; use a private channel instead.
