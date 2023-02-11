# Equivalent to db.py OR app.py in previous projects
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

#Models
from .models import User

@app.route("/")
def hello_world():
    return jsonify(hello="world")