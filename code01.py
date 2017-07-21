# Imports the Google Cloud client library
from google.cloud import language

# Instantiates a client
language_client = language.Client()

while True:
	text = input("Enter text to analyze:- ")
	if not text:
		break;
	else:
         # The text to analyze
         document = language_client.document_from_text(text)
         # Detects the sentiment of the text
         sentiment = document.analyze_sentiment().sentiment
         print('Text: {}'.format(text))
         print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))