import json

from codeq_nlp_api import CodeqClient

# Convert the raw text into a summary using Codeq NLP api. 
# Save summary in a local file.
# extracted_text_fname: Local extracted text file
# summary_text_fname: Summarized text file
def summarize(extracted_text_fname, summary_text_fname):
    
    # Store Codeq credentials in a separate JSON file so it's easier to manage
    # codeq_user_id: user id
    # codeq_user_key: user key
    with open('./codeq-creds/codeq-creds.json') as file:
        data = json.load(file)

    codeq_user_id = data['codeq_user_id']
    codeq_user_key = data['codeq_user_key']

    # Summarize the extracted text
    with open(extracted_text_fname) as extracted_text_file:
        contents = extracted_text_file.read()
    
    client = CodeqClient(codeq_user_id, codeq_user_key)

    pipeline = 'summarize'
    document = client.analyze(contents, pipeline)

    # Create summary file and save locally
    with open(summary_text_fname, 'w') as summary_text_file:
        summary_text_file.write(document.summary)

    print("Saved summarized text to %s..." % (summary_text_fname))
    
