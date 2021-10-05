# docSummarizer

docSummarizer is a Python app that takes a pdf as input, and summarizes the core concepts of that document into a text file.
This can save a reader time as they may not need to read the entire document, or they may elect to use the summarizer as a pre-read so that at the time of their actual first read, they have more background knowledge about the subject.
docSummarizer uses Google Cloud and Codeq NLP APIs.


### Getting started

To run the application, type:
python3 main.py input.pdf
where input.pdf is a file of your choice
When executing the above, two files get generated:
Raw text file. This contains extracted text from the input pdf. Using the example above, a file named input-raw-text.txt is generated
Summarized text file. This contains summary text from the input pdf. Using the example above, a file named input-summarized-text.txt is generated


### Supported languages

English only at the moment.

Code can be relatively easily extended to support:
Afrikaans, Albanian, Arabic, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, Estonian, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Italian, Japanese, Korean, Latvian, Lithuanian, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swedish, Tamil, Telugu Thai, Turkish, Ukrainian, Vietnamese, Yiddish
