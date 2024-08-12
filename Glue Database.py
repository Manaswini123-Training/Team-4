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

# Create a Glue Database
response = glue_client.create_database(
    DatabaseInput={
        'Name': database_name,
        'Description': 'A database for storing metadata of ingested data.'
    }
)

print(f"Glue Database {database_name} created successfully.")

