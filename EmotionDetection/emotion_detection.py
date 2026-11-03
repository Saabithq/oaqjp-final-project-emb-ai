
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def RunSentimentAnalysis():

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector
    response = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Extract dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Return formatted response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
