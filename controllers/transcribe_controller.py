from flask import jsonify
import json

from services import transcription_service, ollama_service


def transcribe_audio(request):
    audio_file = request.files.get("audio")
    audio_link = request.form.get("link")

    if not audio_file and not audio_link:
        return jsonify({"error": "No audio file provided"}), 400

    transcription = transcription_service.get_transcription(audio_file, audio_link)

    summary = ollama_service.get_summary(transcription)

    return {**json.loads(summary), "transcription": transcription}

