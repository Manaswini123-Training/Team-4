import boto3
from botocore.exceptions import NoCredentialsError

# Function to upload a file to an S3 bucket
def upload_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket: S3 bucket name
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize a session using Amazon S3
    s3_client = boto3.client('s3')

    # Try to upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    else:
        print(f"File {file_name} uploaded to {bucket} as {object_name}.")
        return True

# Specify your file path and bucket name
file_path = "C:\\Users\\koush\\Downloads\\Electric_Vehicle_Population_Data.csv"
bucket_name ='electricvehiclesrawdata'

# Call the function to upload the file
upload_to_s3(file_path, bucket_name)
