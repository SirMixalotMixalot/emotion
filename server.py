"""
A simple web app allowing users to get the emotion of a piece of text
Built by Bokang using Flask and WatsonAi

"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection
app = Flask("Emotion Detector")

def emotions_to_messagge(emotions):
    """
    A function to convert the emotions dictoionary to a more paletable form for the user :)
    """
    return f'''For the given statement, the system response is 'anger': {emotions['anger']},
    'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['fear']},
    'joy': {emotions['joy']} and 'sadness': {emotions['joy']}.
    The dominant emotion is <b>{emotions['dominant_emotion']}</b>.'''

@app.route("/")
def render_index():
    """
    a function to render the index.html
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def detect_emotion():
    """ 
    this route takes the textToAnalyze from the request and returns the emotional analysis
    """
    text_to_analyze = request.args['textToAnalyze']
    emotions = emotion_detection.emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return '<b style="color:red;">Invalid text! Please try again!</b>'
    message = emotions_to_messagge(emotions=emotions)
    return message


if __name__ == "__main__":
    app.run(port=5000)
