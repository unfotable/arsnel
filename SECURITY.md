# Security Policy

## Supported versions

Only the latest release on the default branch receives fixes.

## Reporting a vulnerability

Please **do not** open a public issue. Use GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
("Security" tab -> "Report a vulnerability"). Include steps to reproduce and the
affected file. We aim to acknowledge within 5 working days.

## Scope notes

- Curriculum scripts are teaching code that may *demonstrate* insecure patterns
  (e.g. `eval`, mutable defaults) on purpose; these are labelled in the text.
- No script in this repository makes network calls on its own, and exercises
  never write outside a temporary directory.
- The generated site loads web fonts from Google Fonts; remove the `<link>` in
  `arsnel/templates.py` for a fully offline build.
