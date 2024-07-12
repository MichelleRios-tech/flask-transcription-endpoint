from dotenv import load_dotenv

from models import db_utils


def init_transcriptions_db():
    query = """
                CREATE TABLE IF NOT EXISTS transcriptions (
                    id UUID PRIMARY KEY NOT NULL UNIQUE DEFAULT gen_random_uuid(),
                    transcription TEXT,
                    summary TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    link TEXT
                    )
                """
    db_utils.execute_query(query)
