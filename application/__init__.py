from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql://crowdcam:tgosowhw@127.0.0.1:3307/crowdcam')

from . import upload, display, models

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')