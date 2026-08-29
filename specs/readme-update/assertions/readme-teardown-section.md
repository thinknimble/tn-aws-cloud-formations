---
id: readme-teardown-section
parent: readme-update
created: 2026-08-29T21:10:00Z
priority: 1
status: done
depends-on: readme-overview-table
---

# README documents stack teardown for all formations

## Success Criteria

- A "Teardown" or "Deleting a Stack" section exists in the README
- Documents `aws cloudformation delete-stack --stack-name <STACK-NAME>` as the teardown command
- Notes that all resources created by the stack are deleted (no orphans)
- Mentions `aws cloudformation describe-stacks --stack-name <STACK-NAME>` to verify deletion status
- Applies to all three formations (S3, Bedrock, Sandbox) — not repeated per section
