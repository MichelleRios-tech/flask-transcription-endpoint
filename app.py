from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import transcribe_controller
from models import db_init

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

db_init.init_transcriptions_db()


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    return transcribe_controller.transcribe_audio(request)


@app.route("/transcriptions", methods=["GET"])
def get_transcriptions():
    return transcribe_controller.get_transcriptions()


# sanity check endpoint to make sure the server is running
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong!"})


if __name__ == '__main__':
    app.run()
