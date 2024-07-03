# Flask Whisper Transcription Service
This repository contains a proof-of-concept Flask application that transcribes audio using the Faster Whisper model. Please note that this is an experimental project and may be modified frequently.

This repository contains a proof-of-concept Flask application that transcribes audio using the Faster Whisper model. Please note that this is an experimental project and may be modified frequently.

## Installation

1. **Prerequisites**:
    
    - Make sure you have Python 3.8+ installed
2. **Clone the Repository**:
    
    ```bash
    https://github.com/MichelleRios-tech/flask-transcription-endpoint.git
    cd flask-whisper-transcription-endpoint
    ```
    
3. **Install Dependencies**:
    
    - Install Flask and Faster Whisper:
        
        ```bash
        pip install flask faster-whisper
        ```
        

## Usage

1. **Run the Flask App**:
    
    - Start the Flask server:
        
        ```bash
        python Flask-endpoint.py
        ```
        
    - The server will run at `http://localhost:5000`.
2. **Test the Transcription Endpoint**:
    
    - Use the `/transcribe` endpoint to transcribe audio files.
    - Send a POST request with an audio file with the options body, form data, audio as the key and the audio file as the body
    - Example:

        <img width="972" alt="image" src="https://github.com/MichelleRios-tech/flask-transcription-endpoint/assets/10575816/78d0bd94-11b7-4dc8-9692-c41ca7fd3915">

        
3. **View Transcription Results**:
    
    - The response will contain the transcription.

      <img width="769" alt="image" src="https://github.com/MichelleRios-tech/flask-transcription-endpoint/assets/10575816/88ec9c9b-d263-4997-9c33-edca02927f62">


## Important Note

This project is a proof of concept and may undergo significant changes. Use it for experimentation and learning purposes.
