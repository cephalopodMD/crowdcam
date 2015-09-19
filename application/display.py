__author__ = 'acl3qb'

from flask import send_from_directory, render_template
from . import app, db, models

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/viewer/<videoid>')
def viewer(videoid):
    video = models.Video.query\
            .filter(models.Video.VideoID == videoid)\
            .first()
    if video:
        return render_template('viewer.html',
                               videoid=str(video.VideoID),
                               extension=video.Extension,
                               datetime=str(video.Time),
                               lat=str(video.Lat),
                               lng=str(video.Lng))
    else:
        return "error, no such video id"

if __name__ == '__main__':
    pass