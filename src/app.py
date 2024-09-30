from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/healthcheck")
def hello_world():
    kyiv = pytz.timezone('Europe/Kyiv')
    now = datetime.now(kyiv)
    date = now.isoformat('T')
    return {
        "message": date,
        "status":"200 OK",
    }