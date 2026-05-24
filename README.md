# Final Project: Emotion Detector

An AI-based web application built as part of the Final Project for the IBM Generative AI Engineering course. It detects and analyzes emotions expressed in user-submitted text using Python, Flask, and the IBM Watson NLP Runtime API.

## Project Structure

```
Final-Project-01/
├── EmotionDetection/
│   ├── __init__.py           # Package initializer
│   └── emotion_detection.py  # Core Watson NLP emotion detection logic
├── templates/
│   └── index.html            # Web UI
├── server.py                 # Flask application server
├── test_emotion_detection.py # Unit tests
└── README.md
```

## Features

- Detects five emotions: **anger**, **disgust**, **fear**, **joy**, **sadness**
- Returns the **dominant emotion** for each input
- Handles blank/invalid input with a graceful error message (HTTP 400)
- Pylint-compliant code (score 10/10)

## Setup

### Prerequisites

- Python 3.8+
- `pip install flask requests`

### Run the server

```bash
python server.py
```

Open `http://localhost:5000` in your browser.

### Run unit tests

```bash
python -m pytest test_emotion_detection.py -v
```

### Run static code analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

## API

| Endpoint | Method | Parameter | Description |
|---|---|---|---|
| `/emotionDetector` | GET | `textToAnalyze` | Returns emotion scores and dominant emotion |
| `/` | GET | — | Renders the web UI |

## Architecture

- **Backend Core:** Python 3
- **Web Framework:** Flask
- **NLP Integration:** Watson NLP Runtime API (`emotion_aggregated-workflow_lang_en_stock`)
- **Static Code Quality:** PEP8 / Pylint
