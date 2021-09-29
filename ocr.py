import json
import re
from google.cloud import vision
from google.cloud import storage

# Use the Google Cloud Vision APIs to do pdf to text conversion
# gcs_source: Uri of the pdf source file to convert
# gcs_dest: Uri of the destination output that is created by Google Cloud Vision
# pdf_fname: File name of the pdf being processed
def process_pdf(gcs_source, gcs_dest, pdf_fname):
    client = vision.ImageAnnotatorClient()

    batch_size = 20
    mime_type = 'application/pdf'
    feature = vision.Feature(
        type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION
    )

    gcs_source_uri = gcs_source
    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

    gcs_destination_uri = gcs_dest
    gcs_destination = vision.GcsDestination(uri=gcs_destination_uri)
    output_config = vision.OutputConfig(gcs_destination=gcs_destination, batch_size=batch_size)

    async_request = vision.AsyncAnnotateFileRequest(
        features=[feature], input_config=input_config, output_config=output_config
    )

    operation = client.async_batch_annotate_files(requests=[async_request])
    
    print("Extracting text from %s" % (pdf_fname))
    operation.result(timeout=360)

# Extract the text from the Google Cloud Vision generated file
# gcs_dest: Uri of the destination output that is created by Google Cloud Vision
# extracted_text_fname: Raw text file name to be stored locally
def extract_text(gcs_dest, extracted_text_fname):
    storage_client = storage.Client()
    match = re.match(r'gs://([^/]+)/(.+)', gcs_dest)

    # Retrieve the bucket and name of resultant file
    bucket_name = match.group(1)
    prefix = match.group(2)

    bucket = storage_client.get_bucket(bucket_name)
    blob_list = list(bucket.list_blobs(prefix=prefix))

    # Store off to a local temp file for debugging purposes
    with open(extracted_text_fname, "w+") as file:
        for n in range(len(blob_list)):
            output = blob_list[n]

            json_string = output.download_as_string()
            response = json.loads(json_string)

            for m in range(len(response['responses'])):
                page_response = response['responses'][m]
                annotation = page_response['fullTextAnnotation']
                file.write(annotation['text'])

    print("Saved extracted text to %s" % (extracted_text_fname))
