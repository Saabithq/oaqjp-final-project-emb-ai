
Project Name : Final project

# Emotion Detection Application

## Project Description
This project is a Flask-based web application that detects emotions from user-provided text using the IBM Watson Emotion Detection API.

It identifies five emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the dominant emotion.

## Technologies Used
- Python 3.11
- Flask
- IBM Watson Emotion Detection API
- Requests
- HTML, CSS, JavaScript

## Project Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── README.md
└── LICENSE
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Saabithq/oaqjp-final-project-emb-ai.git
```

2. Navigate to the project directory:

```bash
cd oaqjp-final-project-emb-ai
```

3. Install dependencies:

```bash
pip install flask requests
```

## Run the Application

Start the Flask server:

```bash
python3.11 server.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Error Handling

The application handles blank user input.

If the API returns HTTP status code 400, the emotion detector returns `None` for all emotion values.

The application then displays:

```text
Invalid text! Please try again!
```

## Testing

Run the unit tests using:

```bash
python3.11 -m unittest test_emotion_detection.py
```

## Author

**Saabith K.**