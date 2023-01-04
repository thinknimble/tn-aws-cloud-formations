# Create an s3 bucket and required resources 

## Using cli 

<details>
<summary>
Install AWS CLI
</summary>
[Follow These instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
</details>

### CLI Command


`aws cloudformation create-stack --stack-name myteststack3 --template-body file://aws-s3-cloud-formation.yaml  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=paritestonebucket --capabilities CAPABILITY_NAMED_IAM --profile tn`

#### With file 

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-body file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM --profile tn`

#### With URL

`aws cloudformation create-stack --stack-name <STACK-NAME> --template-url file://<FILE-PATH>  --region us-east-1 --parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME> --capabilities CAPABILITY_NAMED_IAM --profile tn`

The following arguments are required: 
`--region <AWS-REGION>` e.g us-east-1 determines where to create the stack 
`--stack-name <STACK-NAME>` this must be unique 
`--parameters ParameterKey=BucketNameParameter,ParameterValue=<BUCKET-NAME>` BUCKET-NAME must be unique and lowercased
`--capabilities CAPABILITY_NAMED_IAM`
`--template-body file://<FILE-PATH>`  path should start with file:// one of `--template-body` or `--template-url`
`--template-url <FILE-URL>` one of `--template-body` or `--template-url`

If you have multiple profiles you will need to also select a profile 
--profile <name> 