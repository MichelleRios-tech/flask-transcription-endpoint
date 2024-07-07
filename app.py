from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
from pytube import YouTube
import json

from services import transcription_service, ollama_service

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    print("Transcribing audio...", request.files, request.form)
    
    audio_file = request.files.get("audio")
    audio_link = request.form.get("link")

    if not audio_file and not audio_link:
        print("No audio file provided")
        return jsonify({"error": "No audio file provided"}), 400

    if audio_file:
        transcription = transcription_service.transcribe_from_file(audio_file)
    else:
        transcription = transcription_service.transcribe_from_youtube(audio_link)
    
    summary = ollama_service.get_summary(transcription)

    json_merged_response = {**json.loads(summary), "transcription": transcription}
    print("summary", summary)

    return json_merged_response

# sanity check endpoint to make sure the server is running
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong!"})

if __name__ == '__main__':
    app.run()
