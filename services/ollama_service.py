import ollama

def get_summary(text):
    stream  = ollama.generate(
        model='mistral',
        prompt='Please generate a summary of the following transcription, identify the main points, instructions and overall idea of the text. if the text touches multiple ideas or instructions list them as bullet points ' + text +
            'also identify if the transcription comes from a multipart conversation, a song, or presentation respond with the next schema in json format: {"summary": summary_text, "type": conversation, song, presentation}',
        stream=True
    )

    return "".join(chunk['response'] for chunk in stream)
