---
id: readme-ci-section
parent: readme-update
created: 2026-08-29T21:00:00Z
priority: 1
status: not_started
depends-on: readme-overview-table
---

# README documents the CI/CD auto-publish workflow

## Success Criteria

- A "CI/CD: Auto-publish to S3" section exists in the README
- Section explains that pushing to main/master triggers automatic upload of all YAML templates to a public S3 bucket
- Required GitHub Actions secrets listed: `AWS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_BUCKET`
- Section explains this is what powers the `--template-url` option in the CLI commands above
