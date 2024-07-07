import os

from faster_whisper import WhisperModel
from pytube import YouTube

model_size = "large-v3"

model = WhisperModel(model_size, device="cuda", compute_type="float16")


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
    audio_file = download_audio_from_youtube(link)
    return generate_transcription(audio_file)

def download_audio_from_youtube(link):
    yt = YouTube(link)
    audio_file = yt.streams.filter(only_audio=True).first().download()
    return audio_file