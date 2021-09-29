import os
import sys
from ocr import *
from summarize import *
from file import *

# Use Google Cloud Services to extract text from a pdf
# Use Codeq NLP api to summarize the text
# Save summarized text into a local text file
# pdf_fname: Name of the pdf file
def main():
    # Pass the applicaition api credentials from Google
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./google-creds/api-account-token.json'
    bucket_name = 'ethan-ocr-api'
    
    args = sys.argv[1:]

    if (len(args) != 1):
        print("Must pass only one parameter. Need to specify the pdf file to be summarized")
        sys.exit()

    pdf_fname = args[0]
    core_file_name = os.path.splitext(pdf_fname)[0]
    extracted_text_fname = core_file_name + '-raw-text.txt'
    summary_text_fname = core_file_name + '-summarized-text.txt'

    #gcs_source is the source pdf file on Google Cloud Storage
    gcs_source = upload_to_gcs(bucket_name, pdf_fname)

    #gcs_dest is the destination json file output by the Google Cloud Vision APIs and stored on Google Cloud Storage
    gcs_dest = get_gcs_link(bucket_name, core_file_name + '.result ')
    
    process_pdf(gcs_source, gcs_dest, pdf_fname)
    extract_text(gcs_dest, extracted_text_fname)
    summarize(extracted_text_fname, summary_text_fname)

if __name__ == "__main__":
    main()

