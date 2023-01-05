# Create an s3 bucket and required resources 

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

`aws cloudformation create-stack --stack-name myteststack3 --template-body file://aws-s3-cloud-formation.yaml  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=paritestonebucket --capabilities CAPABILITY_NAMED_IAM --profile tn`

#### With file 

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM --profile tn`

#### With URL

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-url file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM --profile tn`

The following arguments are required: 
`--stack-name <STACK-NAME>` this must be unique 
`--parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME>` BUCKET-NAME must be unique and lowercased
`--capabilities CAPABILITY_NAMED_IAM`
`--template-body file://<FILE-PATH>`  path should start with file:// one of `--template-body` or `--template-url`
`--template-url <FILE-URL>` one of `--template-body` or `--template-url`



### Get the appropriate output variables 

When the cloud formation is done you can get the Access Key Id, Secret and Bucket name from the outputs 

#### Using the cli 
`aws cloudformation describe-stacks --stack-name <STACK-NAME>` from the previously create command

#### Using the console 

Visit the CloudFormation Dashboard, click into the new stack you created and then tap the Outputs Tab

### Instructions for manual creation (No Cloud Formation)

If you do not want to use the cloud formation here are instructions for manually creating the appropriate resources

[Read on Notion](https://www.notion.so/thinknimble/AWS-b5e1ffd8f06d459788515843fea41418#c723773015fd436c9ba801ba663dda13)