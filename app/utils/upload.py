import os

from app.setup.creds import BUCKET_NAME
from google.cloud import storage

def upload_to_google_cloud_storage(file_path: str, bucket_name: str = BUCKET_NAME):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)
    os.remove(file_path)
    return blob.public_url