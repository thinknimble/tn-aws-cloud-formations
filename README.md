# ThinkNimble AWS CloudFormations

This repository provides AWS CloudFormation configs that streamline the process of creating application resources on AWS that we commonly use in our applications. For instance, it is best practice to create a unique IAM user per app and follow the Principle of Least Privilege, meaning that user's permissions should be limited to only what is needed for the app.

There are currently three configurations and instructions below.

- [Create S3 Bucket](#create-s3-bucket)
- [Create Bedrock Permissions Policy](#create-an-aws-bedrock-permissions-policy)
- [Create Sandbox Instance](#create-sandbox-instance)
- [CI/CD: Auto-publish to S3](#cicd-auto-publish-to-s3)

| Template | Purpose | Section |
|----------|---------|---------|
| `aws-s3-cloud-formation.yaml` | S3 bucket with IAM user and secure bucket policies | [Create S3 Bucket](#create-s3-bucket) |
| `bedrock-user-permissions.yaml` | IAM user with AWS Bedrock permissions | [Create Bedrock Permissions Policy](#create-an-aws-bedrock-permissions-policy) |
| `sandbox-cloud-formation.yaml` | Ubuntu instance in an isolated VPC with SSH access | [Create Sandbox Instance](#create-sandbox-instance) |

These configurations require the AWS CLI. [Follow these instructions to get started](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Create S3 Bucket

Our apps use S3 to store user-uploaded files and other static media. Use this cloud formaiton to quickly spin up a Bucket, IAM User, and secure Bucket Policies.

**Please note if you have multiple aws accounts configured you will need to pass the profile key and if a region is not set the region key**

```term
aws <command> --profile <profile-name> --region <aws-region>
```

#### What you will need

- An aws access key and id with elevated priveleges to be able to run this command
- A name for your cloud formation stack that is unique and in all caps
- A name for your s3 bucket

Things to consider:

- If you have multiple aws accounts you will need to pass in your profile --profile <name> to the args
- If you do not have a default region set up you will also need to pass that in

### CLI Command Using the YAML File

For this to work, you will need to download the YAML file or clone this repository.

If you are setting this up on an aws account that does not have the file stored in its own S3 you will need to use the local file.

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> ParameterKey=EnableEncryption,ParameterValue=true --capabilities CAPABILITY_NAMED_IAM
```

### CLI Command Using the URL

For convenience, the configs are also available on a public S3 bucket, so that you do not need to download them.

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/aws-s3-cloud-formation.yaml'  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> ParameterKey=EnableEncryption,ParameterValue=true --capabilities CAPABILITY_NAMED_IAM
```

The following arguments are required:

- `--stack-name <STACK-NAME>` this must be unique
- `--parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME>` BUCKET-NAME must be unique and lowercased
- `--capabilities CAPABILITY_NAMED_IAM`
- `--template-body file://<FILE-PATH>` path should start with file:// one of `--template-body` or `--template-url`
- `--template-url <FILE-URL>` one of `--template-body` or `--template-url`

Optional parameters:

- `ParameterKey=EnableEncryption,ParameterValue=true` enables AES-256 server-side encryption on the bucket (default: `false`)

### Using the AWS Console

You can also run the "stack" from the AWS Console:

- Visit the console, sign in and navigate to the CloudFormation Dashboard
- Click create stack (with new resources)
- select Template is ready
- Select Amazon S3 URL and provide the yaml file from this repo uploaded to S3 as the [link](https://tn-s3-cloud-formation.s3.amazonaws.com/aws-s3-cloud-formation.yaml)
- Click next and pass in the required parameter value (S3 Bucket Name)

### Get the appropriate output variables

When the cloud formation is done you can get the Access Key ID, Secret, and Bucket name from the outputs

#### Using the cli

Quick command to get just the outputs:

```term
aws cloudformation describe-stacks --stack-name <STACK-NAME> --query "Stacks[0].Outputs" --output table
```

Or as JSON:

```term
aws cloudformation describe-stacks --stack-name <STACK-NAME> --query "Stacks[0].Outputs"
```

#### Using the console

Visit the CloudFormation Dashboard, click into the new stack you created and then tap the Outputs Tab

### Instructions for manual creation (No Cloud Formation)

If you do not want to use the cloud formation here are instructions for manually creating the appropriate resources

[Read on Notion](https://www.notion.so/thinknimble/AWS-b5e1ffd8f06d459788515843fea41418#c723773015fd436c9ba801ba663dda13)

## Create an AWS Bedrock Permissions Policy

Our apps use AWS Bedrock for fast and low-cost LLM features. An IAM User with the proper permissions is required.

## Setup

First, an AWS Administrator will need to enable Amazon Bedrock organization-wide. They will have to request access to the models we want to use. To do this: Go to AWS Bedrock in the console and follow the instructions there. We have already done this for ThinkNimble's AWS accounts in us-east-1.

### With File

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://bedrock-user-permissions.yaml  --region us-east-1 --parameters ParameterKey=ProjectName,ParameterValue=<PROJECTNAME> ParameterKey=AllowedModels,ParameterValue=<SOME_MODEL_ARN_OR_*_FOR_DEFAULT_ALL> --capabilities CAPABILITY_NAMED_IAM
```

### With URL

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/bedrock-user-permissions.yaml' --region us-east-1 --parameters ParameterKey=ProjectName,ParameterValue=<PROJECTNAME> ParameterKey=AllowedModels,ParameterValue=<SOME_MODEL_ARN_OR_*_FOR_DEFAULT_ALL>  --capabilities CAPABILITY_NAMED_IAM
```

### Check Status & Outputs with File

```term
aws cloudformation describe-stacks --stack-name <STACK-NAME>
```

## Create Sandbox Instance

Launches an Ubuntu 24.04 EC2 instance in an isolated VPC with SSH-only ingress. Useful for creating disposable development sandboxes.

#### What you will need

- An AWS access key and ID with elevated privileges to run this command
- A name for your CloudFormation stack that is unique
- An existing EC2 key pair for SSH access
- The CIDR block you want to allow SSH from (e.g. your IP as `203.0.113.5/32`)

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `KeyPairName` | Yes | — | Name of an existing EC2 key pair for SSH access |
| `SSHSourceCIDR` | Yes | — | CIDR block allowed to SSH into the instance (e.g. `203.0.113.0/32`) |
| `InstanceType` | No | `t3.medium` | EC2 instance type |
| `ExistingVpcId` | No | — | ID of an existing VPC to launch into (skips VPC creation) |
| `ExistingSubnetId` | No | — | ID of a subnet in the existing VPC (required when `ExistingVpcId` is set) |

### CLI Command Using the YAML File

For this to work, you will need to download the YAML file or clone this repository.

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://sandbox-cloud-formation.yaml --region us-east-1 --parameters ParameterKey=KeyPairName,ParameterValue=<KEY-PAIR-NAME> ParameterKey=SSHSourceCIDR,ParameterValue=<YOUR-CIDR> --capabilities CAPABILITY_NAMED_IAM
```

### CLI Command Using the URL

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/sandbox-cloud-formation.yaml' --region us-east-1 --parameters ParameterKey=KeyPairName,ParameterValue=<KEY-PAIR-NAME> ParameterKey=SSHSourceCIDR,ParameterValue=<YOUR-CIDR> --capabilities CAPABILITY_NAMED_IAM
```

### Using an Existing VPC

By default, the sandbox template creates a new VPC for each stack. AWS accounts have a default limit of 5 VPCs per region, so if you are creating multiple sandboxes you can hit that limit quickly. To avoid this, pass `ExistingVpcId` and `ExistingSubnetId` to launch the instance into a VPC you already have:

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://sandbox-cloud-formation.yaml --region us-east-1 --parameters ParameterKey=KeyPairName,ParameterValue=<KEY-PAIR-NAME> ParameterKey=SSHSourceCIDR,ParameterValue=<YOUR-CIDR> ParameterKey=ExistingVpcId,ParameterValue=<VPC-ID> ParameterKey=ExistingSubnetId,ParameterValue=<SUBNET-ID> --capabilities CAPABILITY_NAMED_IAM
```

**Note:** The existing subnet must have internet access (via an Internet Gateway route) and auto-assign public IP addresses enabled, so the instance is reachable over SSH.

### Outputs

| Output | Description |
|--------|-------------|
| `PublicIP` | Public IP address of the sandbox instance |
| `InstanceId` | EC2 instance ID |
| `SpekkCommand` | Command to register the sandbox with the spekk CLI |

The `SpekkCommand` output provides a ready-to-paste command that registers the new sandbox instance with the spekk CLI, so you can manage it via `spekk sandbox` commands.

To retrieve outputs after the stack is created:

```term
aws cloudformation describe-stacks --stack-name <STACK-NAME> --query "Stacks[0].Outputs" --output table
```

## CI/CD: Auto-publish to S3

Pushing to `main` or `master` triggers a GitHub Actions workflow that automatically uploads all YAML templates in this repository to a public S3 bucket. This is what powers the `--template-url` option in the CLI commands above — templates stay up to date without manual uploads.

The workflow lives in `.github/workflows/upload_to_s3.yaml`.

### Required GitHub Actions Secrets

| Secret | Description |
|--------|-------------|
| `AWS_KEY_ID` | IAM access key ID with S3 write permissions |
| `AWS_SECRET_ACCESS_KEY` | Corresponding secret access key |
| `AWS_BUCKET` | Target S3 bucket name (e.g. `tn-s3-cloud-formation`) |

Configure these in your repository's **Settings > Secrets and variables > Actions**.
