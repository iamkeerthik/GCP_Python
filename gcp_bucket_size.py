from google.cloud import storage
import math
from openpyxl import Workbook

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
project_id = 'quickstart-1559963030019'

# Initialize a client object to interact with GCP Storage
client = storage.Client(project=project_id)

# Get all buckets in the project
buckets = client.list_buckets()

# Create a new workbook and worksheet
wb = Workbook()
ws = wb.active

# Write the headers to the worksheet
ws.append(['Bucket Name', 'Total Size'])

# Write the size of each bucket in MB, GB, and KB to the worksheet
for bucket in buckets:
    total_size = sum(blob.size for blob in bucket.list_blobs())
    ws.append([bucket.name, format_size(total_size)])

# Save the workbook to a file with the project ID as the file name
wb.save(f'{project_id}.xlsx')
