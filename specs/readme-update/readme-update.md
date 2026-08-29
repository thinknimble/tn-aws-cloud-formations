---
id: readme-update
created: 2026-08-29T21:00:00Z
priority: 1
---

# README reflects all formations and CI automation

The README is the entry point for anyone using this repo. It currently documents two of three CloudFormation templates and omits the CI/CD pipeline entirely.

## Formations to document

| Template | Purpose |
|---|---|
| `aws-s3-cloud-formation.yaml` | S3 bucket + IAM user (already documented) |
| `bedrock-user-permissions.yaml` | Bedrock IAM policy + user (already documented) |
| `sandbox-cloud-formation.yaml` | Ubuntu 24.04 EC2 in isolated VPC with SSH access (**missing**) |

## CI/CD to document

The GitHub Action `.github/workflows/upload_to_s3.yaml` auto-publishes all YAML templates to a public S3 bucket on push to main. This powers the `--template-url` option in every formation's docs. Not documented anywhere in the README.

## Style

Each formation section follows the same pattern established by the S3 Bucket section: description, parameters, CLI with file, CLI with URL, outputs. The sandbox section should follow this pattern.
