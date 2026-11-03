
import requests
import json


def sentiment_analyzer(text_to_analyze):

    # Define the URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Define headers
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Handle blank input (status code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert response text into JSON
    formatted_response = json.loads(response.text)

    # Extract emotion values
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
