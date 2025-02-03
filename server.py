from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    data = request.json  # Récupérer le JSON envoyé dans la requête
    text_to_analyze = data.get("text", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)

    response_text = f"For the given statement, the system response is " \
                    f"'anger': {result['anger']}, 'disgust': {result['disgust']}, " \
                    f"'fear': {result['fear']}, 'joy': {result['joy']}, " \
                    f"'sadness': {result['sadness']}. " \
                    f"The dominant emotion is {result['dominant_emotion']}."

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
