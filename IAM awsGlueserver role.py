import boto3
import json

iam_client = boto3.client('iam')

# Define role name
role_name = 'AWSGlueServiceRole'

# Create the role with the specified trust policy
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "glue.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

response = iam_client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy),
    Description='Role for AWS Glue with the necessary permissions'
)

print(f"Created role: {response['Role']['Arn']}")
