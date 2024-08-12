import boto3
import json

iam_client = boto3.client('iam')

role_name='AWSGlueServiceRole'

# Attach the AWSGlueServiceRole policy
iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
)

# Attach additional policies if needed
iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'  # For S3 access
)
