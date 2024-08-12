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


response = glue_client.get_tables(DatabaseName=database_name)
for table in response['TableList']:
    print(f"Table: {table['Name']}")
    print(f"Columns: {[col['Name'] for col in table['StorageDescriptor']['Columns']]}")
