from flask import Flask, render_template

app = Flask(__name__)

from . import upload, display

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')