---
id: readme-sandbox-section
parent: readme-update
created: 2026-08-29T21:00:00Z
priority: 1
status: in_progress
depends-on: readme-overview-table
locked-by: builder-MacBook-Pro.local-44193-1788033815
---

# README documents the sandbox CloudFormation template

## Success Criteria

- A "Create Sandbox Instance" section exists in the README following the same structure as the S3 Bucket section
- Section describes purpose: launches an Ubuntu 24.04 EC2 instance in an isolated VPC with SSH-only ingress
- Parameters documented: `InstanceType` (default `t3.medium`), `KeyPairName` (required), `SSHSourceCIDR` (required, CIDR format)
- CLI command with `--template-body file://` shown with all required parameters
- CLI command with `--template-url` shown pointing to the public S3 URL for `sandbox-cloud-formation.yaml`
- Outputs documented: `PublicIP`, `InstanceId`, `SpekkCommand`
- The `SpekkCommand` output is explained (registers sandbox with spekk CLI)
