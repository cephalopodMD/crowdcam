__author__ = 'acl3qb'

import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from . import app

UPLOAD_FOLDER = '/var/www/html/crowdcam/videofiles'
ALLOWED_EXTENSIONS = set(['mp4','mpeg4','H264'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('uploads.html')