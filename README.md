# Create an s3 bucket and required resources 

Use this cloud formaiton to quickly spin up the appropriate resources (IAM,Bucket,Bucket Policies etc) for a webapp using AWS storage

## Using cli 

<details>
<summary>
Install AWS CLI
</summary>
[Follow These instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
</details>

**Please note if you have multiple aws accounts configured you will need to pass the profile key and if a region is not set the region key**

`aws <command> --profile <profile-name> --region <aws-region>`

### CLI Command
#### With file 

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM`

#### With URL

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-url 'https://tn-s3-cloud-formation.s3.amazonaws.com/aws-s3-cloud-formation.yaml'  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM`

The following arguments are required: 

- `--stack-name <STACK-NAME>` this must be unique 
- `--parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME>` BUCKET-NAME must be unique and lowercased
- `--capabilities CAPABILITY_NAMED_IAM`
- `--template-body file://<FILE-PATH>`  path should start with file:// one of `--template-body` or `--template-url`
- `--template-url <FILE-URL>` one of `--template-body` or `--template-url`

### Using the AWS Console
- visit the console, sign in and navigate to the CloudFormation Dashboard
- Click create stack (with new resources)
- select Template is ready
- Select Amazon S3 URL and provide the yaml file from this repo uploaded to S3 as the [link](https://tn-s3-cloud-formation.s3.amazonaws.com/aws-s3-cloud-formation.yaml)
- Click next and pass in the required parameter value (S3 Bucket Name)

### Get the appropriate output variables 

When the cloud formation is done you can get the Access Key Id, Secret and Bucket name from the outputs 

#### Using the cli 
`aws cloudformation describe-stacks --stack-name <STACK-NAME>` from the previously create command

This will return a json object to retrieve the variables tab down to the `Outputs` key

#### Using the console 

Visit the CloudFormation Dashboard, click into the new stack you created and then tap the Outputs Tab

### Video instructions
https://www.loom.com/share/f335244216264794aa78c0af8afbdffd

### Instructions for manual creation (No Cloud Formation)

If you do not want to use the cloud formation here are instructions for manually creating the appropriate resources

[Read on Notion](https://www.notion.so/thinknimble/AWS-b5e1ffd8f06d459788515843fea41418#c723773015fd436c9ba801ba663dda13)
