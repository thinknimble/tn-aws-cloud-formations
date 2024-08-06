# ThinkNimble AWS CloudFormations

This repository provides AWS CloudFormation configs that streamline the process of creating application resources on AWS that we commonly use in our applications. For instance, it is best practice to create a unique IAM user per app and follow the Principle of Least Privilege, meaning that user's permissions should be limited to only what is needed for the app.

There are currently two configurations and instructions below.

- [Create S3 Bucket](#create-s3-bucket)
- [Create Bedrock Permissions Policy](#create-a-bedrock-permissions-policy)

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
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM
```

### CLI Command Using the URL

For convenience, the configs are also available on a public S3 bucket, so that you do not need to download them.

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/aws-s3-cloud-formation.yaml'  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM
```

The following arguments are required:

- `--stack-name <STACK-NAME>` this must be unique
- `--parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME>` BUCKET-NAME must be unique and lowercased
- `--capabilities CAPABILITY_NAMED_IAM`
- `--template-body file://<FILE-PATH>` path should start with file:// one of `--template-body` or `--template-url`
- `--template-url <FILE-URL>` one of `--template-body` or `--template-url`

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

`aws cloudformation describe-stacks --stack-name <STACK-NAME>` from the previously create command

This will return a json object to retrieve the variables tab down to the `Outputs` key

#### Using the console

Visit the CloudFormation Dashboard, click into the new stack you created and then tap the Outputs Tab

### Instructions for manual creation (No Cloud Formation)

If you do not want to use the cloud formation here are instructions for manually creating the appropriate resources

[Read on Notion](https://www.notion.so/thinknimble/AWS-b5e1ffd8f06d459788515843fea41418#c723773015fd436c9ba801ba663dda13)

## Create an AWS Bedrock Permissions Policy

Our apps use AWS Bedrock for fast and low-cost LLM features. An IAM User with the proper permissions is required.

## Setup

First, an AWS Administrator will need to enable Amazon Bedrock organization-wide. They will have to request access to the models we want to use. To do this: Go to AWS Bedrock in the console and follow the instructions there. I've done this for our TN Staging and Production AWS orgs

### With File

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://bedrock-user-permissions.yaml  --region us-east-1 --parameters ParameterKey=ProjectName,ParameterValue=<PROJECTNAME> ParameterKey=<SOME_MODEL_ARN_OR_*_FOR_DEFAULT_ALL>  --capabilities CAPABILITY_NAMED_IAM
```

### With URL

```term
aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/bedrock-user-permissions.yaml' --region us-east-1 --parameters ParameterKey=ProjectName,ParameterValue=<PROJECTNAME> ParameterKey=<SOME_MODEL_ARN_OR_*_FOR_DEFAULT_ALL>  --capabilities CAPABILITY_NAMED_IAM
```

### Check Status & Outputs with File

```term
aws cloudformation describe-stacks --stack-name <STACK-NAME>
```
