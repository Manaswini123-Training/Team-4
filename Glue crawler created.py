# Define crawler name and S3 target path
import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='AKIAW3MEEUPP7PWKIAF2',
    aws_secret_access_key='Q6v8a69Fi26E8ggOQWpguVn6AMMuCbffN37ypRDY',
    region_name='us-east-2'  # Choose your preferred region
)
# Create a Glue client
glue_client = session.client('glue')

# Define the Glue Database name
database_name = 'electricvehicles_database'

crawler_name = 'ev-data-crawler'
bucket_name='electricvehiclesrawdata'
s3_target_path = f's3://{bucket_name}/raw-data/'

# Create Glue crawler
glue_client.create_crawler(
    Name=crawler_name,
    Role='AWSGlueServiceRole',
    DatabaseName=database_name,
    Targets={'S3Targets': [{'Path': s3_target_path}]}
)

# Start the crawler
glue_client.start_crawler(Name=crawler_name)
