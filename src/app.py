from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

if os.environ.get("mode") == "local":
    app.run(host="127.0.0.1", port=8002)
