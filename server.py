"""
Server module for the Emotion Detection web application.

This Flask application provides an API endpoint to analyze emotions from a given text.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """Endpoint for analyzing emotions from a given text.

    This function receives a JSON payload containing text, processes it using
    the emotion_detector function, and returns the detected emotions.

    Returns:
        JSON response with emotion scores and dominant emotion.
    """
    data = request.json
    text_to_analyze = data.get("text", "").strip()

    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = f"For the given statement, the system response is " \
                    f"'anger': {result['anger']}, 'disgust': {result['disgust']}, " \
                    f"'fear': {result['fear']}, 'joy': {result['joy']}, " \
                    f"'sadness': {result['sadness']}. " \
                    f"The dominant emotion is {result['dominant_emotion']}."

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
