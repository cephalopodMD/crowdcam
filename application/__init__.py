from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql://crowdcam:tgosowhw@127.0.0.1:3307/crowdcam')

VIDEO_FOLDER = os.path.join(os.getcwd(),'videofiles')
THUMBNAIL_FOLDER = os.path.join(os.getcwd(),'thumbnails')
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER
app.config['THUMBNAIL_FOLDER'] = THUMBNAIL_FOLDER

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

from . import upload, display, models

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')