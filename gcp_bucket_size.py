from google.cloud import storage
import math

def format_size(size):
    """Converts size in bytes to human-readable format"""
    if size < 1024:
        return "{:.2f} B".format(size)
    elif size < 1024**2:
        return "{:.2f} KB".format(size/1024)
    elif size < 1024**3:
        return "{:.2f} MB".format(size/1024**2)
    elif size < 1024**4:
        return "{:.2f} GB".format(size/1024**3)
    else:
        return "{:.2f} TB".format(size/1024**4)

# Specify the project ID
project_id = 'your-project-id'

# Initialize a client object to interact with GCP Storage
client = storage.Client(project=project_id)

# Get all buckets in the project
buckets = client.list_buckets()

# Print the size of each bucket in MB, GB, and KB
for bucket in buckets:
    total_size = sum(blob.size for blob in bucket.list_blobs())
    print("{}: {}".format(bucket.name, format_size(total_size)))
