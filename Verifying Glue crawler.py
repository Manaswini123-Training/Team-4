import boto3

# Initialize the Glue client
glue_client = boto3.client('glue', region_name='us-east-2')  # Replace 'us-west-2' with your region

def check_crawler_status(crawler_name):
    try:
        # Get the crawler details
        response = glue_client.get_crawler(Name=crawler_name)
        crawler_info = response['Crawler']
        
        # Extract and print the crawler's state
        crawler_state = crawler_info['State']
        print(f"Crawler '{crawler_name}' status: {crawler_state}")
        
        return crawler_state
    except glue_client.exceptions.EntityNotFoundException:
        print(f"Crawler '{crawler_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the crawler name
crawler_name = 'ev-data-crawler'  # Replace with your crawler name

# Check the status of the crawler
check_crawler_status(crawler_name)
