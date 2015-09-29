__author__ = 'acl3qb'

import os
from flask import Flask, request, redirect, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
from . import app, db, models

ALLOWED_EXTENSIONS = set(['mp4','mpeg4','mpeg','H264'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            extension = (file.filename).rsplit('.', 1)[1]
            video = models.Video(0,
                                 datetime.utcnow(),
                                 request.form['lat'],
                                 request.form['lng'],
                                 extension)
            db.session.add(video)
            db.session.commit()
            # save by video id using the extension from earlier
            filename = str(video.VideoID) + '.' + extension
            # we can load it from wild cards for the hackathon
            file.save(os.path.join(app.config['VIDEO_FOLDER'],filename))
            # thumbnails
            os.popen('avconv -i ' +
                     os.path.join(app.config['VIDEO_FOLDER'], filename) +
                     ' -ss 00:00:00 -vframes 1 ' +
                     os.path.join(app.config['THUMBNAIL_FOLDER'], str(video.VideoID)) +
                     '.jpeg')
            return redirect('/viewer/'+str(video.VideoID))
    return render_template('uploads.html')