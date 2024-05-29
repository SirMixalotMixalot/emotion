import requests
import json

EMPTY_EMOTIONS = {
        'anger':None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
}
def emotion_detector(text_to_analyse: str):
    if len(text_to_analyse) == 0:
        return EMPTY_EMOTIONS
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 400 or response.status_code == 500:
        return EMPTY_EMOTIONS
    parsed_response =  json.loads(response.text)
    emotions_dict = parsed_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions_dict, key=lambda k: float(emotions_dict[k]))
    return {
        'anger': emotions_dict['anger'],
        'disgust': emotions_dict['disgust'],
        'fear': emotions_dict['fear'],
        'joy': emotions_dict['joy'],
        'sadness': emotions_dict['sadness'],
        'dominant_emotion': dominant_emotion
    }