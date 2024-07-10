import ollama


def get_summary(text):
    prompt = ('Please generate a summary of the following transcription, identify the main points, instructions and '
              'overall idea of the text.' '') + text + (
                 'also identify if the transcription comes from a multipart conversation, a song, '
                 'or presentation, respond with the next schema in json format: {"summary": summary_text, '
                 '"type": conversation, song, presentation}')

    return generate_answer(prompt)


def generate_answer(prompt):
    stream = ollama.generate(
        model='mistral',
        prompt=prompt,
        stream=True
    )

    return "".join(chunk['response'] for chunk in stream)
