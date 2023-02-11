# Equivalent to db.py OR app.py in previous projects
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")