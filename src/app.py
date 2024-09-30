from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/healthcheck")
def hello_world():
    now = datetime.now()
    date = now.isoformat('T')
    return {
        "message": date,
        "status":"200 OK",
    }