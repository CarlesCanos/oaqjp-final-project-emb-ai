"""Server to check text emotions"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Function returning index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Function returning analysis from text"""
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)

    if response['dominant_emotion'] == 'None':
        return 'Invalid text! Please try again!'


    return  (
            f"For the given statement, the system response is "
            f"anger: {response['anger']}, "
            f"disgust: {response['disgust']}, "
            f"fear: {response['fear']}, "
            f"joy: {response['joy']}, "
            f"sadness: {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
