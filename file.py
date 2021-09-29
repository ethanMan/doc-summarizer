from google.cloud import storage

# Upload the local file to Google Cloud Storage for future processing
# bucket_name: Bucket name in Google Cloud Storage
# local_fname: Local file to be uploaded to Google Cloud Storage
# Returns the gs:// file url
def upload_to_gcs(bucket_name, local_fname):
    storage_client = storage.Client()
    
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(local_fname)
    blob.upload_from_filename(local_fname)

    return get_gcs_link(bucket_name, local_fname)

# Create the Google Cloud Storage url
# bucket_name: Bucket name in Google Cloud Storage
# local_fname: Local file to be uploaded to Google Clout Storage
# Returns the gs:// file url
def get_gcs_link(bucket_name, local_fname):
    # Need to construct the Google Cloud Storage url manually
    return 'gs://' + bucket_name + '/' + local_fname
