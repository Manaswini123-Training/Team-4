
import boto3

def create_bucket(bucket_name, region='us-east-2'):
    """Create an S3 bucket in a specified region"""
    
    # Initialize the S3 client
    s3_client = boto3.client('s3', region_name='us-east-2')
    
    try:
        # Create bucket
        if region is None:
            response = s3_client.create_bucket(Bucket='electricvehiclesrawdata')
        else:
            response = s3_client.create_bucket(
                Bucket='electricvehiclesrawdata',
                CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}
            )
        
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")


