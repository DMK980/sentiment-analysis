"""
    This module is for interacting with 
    the Watson NLP model for text sentiment
    analysis.

"""
# imports for the program
import requests

# Method for sending the post request
def sentiment_analyzer(text_to_analyse):
    """
        This method calls the watson API
        to retrieve a response from the 
        NLP model

    """

    # required parameters
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    my_input = {"raw_document":{"text":text_to_analyse}}

    # calling the API
    response = requests.post(url,json = my_input, headers=header)

    # returns an object response.
    return response.text