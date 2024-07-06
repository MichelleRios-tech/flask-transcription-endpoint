import os

from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
from pytube import YouTube

app = Flask(__name__)
model_size = "large-v3"

model = WhisperModel(model_size, device="cuda", compute_type="float16")


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    print("Transcribing audio...", request.files, request.form)
    
    audio_file = request.files.get("audio")
    audio_link = request.form.get("link")

    if not audio_file and not audio_link:
        print("No audio file provided")
        return jsonify({"error": "No audio file provided"}), 401

    if audio_file:
        transcription = transcribe_from_file(audio_file)
    else:
        transcription = transcribe_from_youtube(audio_link)

    return jsonify({"transcription": transcription})

def transcribe_from_file(audio_file):
    print("Transcribing audio file", audio_file.filename)
    filename = audio_file.filename + ".mp3"
    audio_file.save(filename)

    return generate_transcription(filename)

def generate_transcription(filename):
    segments, _ = model.transcribe(filename, beam_size=5)
    os.remove(filename)
    print(f"File {filename} removed successfully.")
    return " ".join(segment.text for segment in segments)

def transcribe_from_youtube(link):
    print("Downloading audio from YouTube link", link)
    yt = YouTube(link)
    audio_file = yt.streams.filter(only_audio=True).first().download()

    return generate_transcription(audio_file)

if __name__ == '__main__':
    app.run()