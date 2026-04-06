import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    # Set the headers with the required model ID for the API
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text into a dictionary using json library
    response_dict = json.loads(response.text)
    
    # Check if the response contains an error or if emotionPredictions is missing
    if 'emotionPredictions' not in response_dict:
        # Return None values for all emotions if there's an error
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Extract the required set of emotions from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the formatted output with all emotions and dominant emotion
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }