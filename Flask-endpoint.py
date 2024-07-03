import os

from flask import Flask, request, jsonify
from faster_whisper import WhisperModel

app = Flask(__name__)
model_size = "large-v3"

model = WhisperModel(model_size, device="cuda", compute_type="float16")


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    filename = audio_file.filename + ".mp3"

    if audio_file:
        audio_file.save(filename)

        segments, info = model.transcribe(filename, beam_size=5)
        os.remove(filename)
        print(f"File {filename} removed successfully.")
        transcription = " ".join(segment.text for segment in segments)

        return jsonify({"transcription": transcription})
