import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/var/www/html/crowdcam/videofiles'
ALLOWED_EXTENSIONS = set(['mp4','mpeg4','H264'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import urls
