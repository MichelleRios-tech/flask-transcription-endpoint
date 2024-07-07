import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from transcription_service import transcribe_from_file, transcribe_from_youtube


class TranscriptionServiceTests(unittest.TestCase):
    @patch("transcription_service.generate_transcription", return_value = "This is a test transcription")
    def test_transcribe_from_file(self, generate_transcription_mock):
        audio_file = MagicMock()
        audio_file.filename = "test_audio.wav"

        audio_file.save = MagicMock()

        generate_transcription = generate_transcription_mock

        result = transcribe_from_file(audio_file)

        audio_file.save.assert_called_once_with("test_audio.wav.mp3")

        generate_transcription.assert_called_once_with("test_audio.wav.mp3")

        self.assertEqual(result, "This is a test transcription")

        generate_transcription_mock.stop()

    @patch("transcription_service.download_audio_from_youtube", return_value = "test_audio.wav.mp3")
    @patch("transcription_service.generate_transcription", return_value = "This is a test transcription")
    def test_transcribe_from_youtube(self, generate_transcription_mock, download_audio_from_youtube_mock):
        link = "https://www.youtube.com/watch?v=12345"

        download_audio_from_youtube = download_audio_from_youtube_mock
        
        generate_transcription = generate_transcription_mock

        result = transcribe_from_youtube(link)

        download_audio_from_youtube.assert_called_once_with(link)

        generate_transcription.assert_called_once_with("test_audio.wav.mp3")

        self.assertEqual(result, "This is a test transcription")

if __name__ == "__main__":
    unittest.main()