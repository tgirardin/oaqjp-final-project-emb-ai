import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        return {"error": f"Request failed with status code {response.status_code}"}

    # Convertir la réponse JSON en dictionnaire
    response_data = response.json()
    print("API Response:", response_data)  # Debugging

    # Extraire les scores des émotions
    emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})

    # Vérifier si l'API a retourné des émotions
    if not emotions:
        return {"error": "No emotion data found in API response"}

    # Trouver l'émotion dominante
    dominant_emotion = max(emotions, key=emotions.get)

    # Retourner le format requis n
    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion
    }
