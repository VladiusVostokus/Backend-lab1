from flask import Flask

app = Flask(__name__)

@app.route("/healthcheck")
def hello_world():
    return {
        "message":"I am working",
        "status":"OK",
    }