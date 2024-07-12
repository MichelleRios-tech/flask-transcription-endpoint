from models import db_utils


def save_new_transcription(transcription):
    query = """
        INSERT INTO transcriptions (transcription, summary, link)
        VALUES (%s, %s, %s)
        """
    params = (transcription["transcription"], transcription["summary"], transcription["link"])

    db_utils.execute_query(query, params)


def get_all_transcriptions():
    query = """
        SELECT * FROM transcriptions
        """
    return db_utils.execute_query(query, return_result=True)
