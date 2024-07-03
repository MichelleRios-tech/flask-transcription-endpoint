import os
import torch

from flask import Flask, request, jsonify
from faster_whisper import WhisperModel

app = Flask(__name__)
model_size = "large-v3"

device = "cuda" if torch.cuda.is_available() else "cpu"

compute_type = "int8" if device == "cpu" else "float16"

model = WhisperModel(model_size, device=device, compute_type=compute_type)


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    filename = audio_file.filename + ".mp3"

    if audio_file:
        audio_file.save(filename)

        segments, _ = model.transcribe(filename, beam_size=5)
        os.remove(filename)
        print(f"File {filename} removed successfully.")
        transcription = " ".join(segment.text for segment in segments)

        return jsonify({"transcription": transcription})

@app.route("/", methods=["GET"])
def hello():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run()