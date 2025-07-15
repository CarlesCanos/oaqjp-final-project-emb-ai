import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = body, headers=headers)
    
    print(response)

    if "400" in str(response):
        return {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None',
            'dominant_emotion': 'None'
            }
    else:
        formatted_response = json.loads(response.text)

        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        emotionLabels = ['anger', 'disgust', 'fear', 'joy', 'sadness']

        currentDominant = 0
        currentDominantIndex = 0

        for index, emotion in  enumerate(emotions):
            if emotion > currentDominant:
                currentDominant = emotion
                currentDominantIndex = index
                
        dominant_emotion = emotionLabels[currentDominantIndex]

        return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
                }