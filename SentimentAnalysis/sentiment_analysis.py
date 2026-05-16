import requests  # Import the requests library to handle HTTP requests
import json

def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of the given text.

    Args:
        text_to_analyse (str): Text to analyze

    Returns:
        str: Response text from the sentiment analysis API
    """

    # URL of the sentiment analysis service
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    # Create a dictionary with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Set the headers required for the API request
    header = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    