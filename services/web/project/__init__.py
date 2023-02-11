# Equivalent to db.py OR app.py in previous projects
from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

#Models
from .models import User

@app.route("/")
def hello_world():
    return jsonify(hello="world")

# Route For Development. In Production, Nginx serves static files
# @app.route("/static/<path:filename>")
# def staticfile(filename):
#     send_from_directory(app.config["STATIC_FOLDER"], filename)

# @app.route('/media/<path:filename>')
# def mediafiles(filename):
#     return send_from_directory(app.config["MEDIA_FOLDER"], filename)
