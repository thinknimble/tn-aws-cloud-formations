import os
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
BUCKET = os.environ.get('BUCKET')



def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('aws-s3-cloud-formation.yaml', BUCKET, 'aws-s3-cloud-formation.yaml')
uploaded = upload_to_aws('bedrock-user-permissions.yaml', BUCKET, 'bedrock-user-permissions.yaml')
