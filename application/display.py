__author__ = 'acl3qb'

from flask import send_from_directory, render_template, jsonify
from sqlalchemy.sql import func
from datetime import datetime
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
        return render_template('viewer.html',videos=[video.dictionary()])
    else:
        return "error, no such video id"

@app.route('/event/<eventid>')
def event_viewer(eventid):
    event = models.Event.query\
        .filter(models.Event.EventID == eventid)\
        .first()
    videos = models.Video.query\
        .filter(models.Video.Lat > float(event.LatStart),
                models.Video.Lat < float(event.LatEnd),
                models.Video.Lng > float(event.LngStart),
                models.Video.Lng < float(event.LngEnd),
                func.unix_timestamp(models.Video.Time) > (event.TimeStart-datetime(1970,1,1)).total_seconds(),
                func.unix_timestamp(models.Video.Time) < (event.TimeEnd-datetime(1970,1,1)).total_seconds())\
        .order_by(models.Video.Time)
    if videos.count() > 0:
        return render_template('viewer.html',
                               videos=[video.dictionary() for video in videos],
                               name=event.Name)
    else:
        return "no videos in this event"


@app.route('/event/<eventid>.json')
def event_json(eventid):
    event = models.Event.query\
        .filter(models.Event.EventID == eventid)\
        .first()
    videos = models.Video.query\
        .filter(models.Video.Lat > float(event.LatStart),
                models.Video.Lat < float(event.LatEnd),
                models.Video.Lng > float(event.LngStart),
                models.Video.Lng < float(event.LngEnd),
                func.unix_timestamp(models.Video.Time) > (event.TimeStart-datetime(1970,1,1)).total_seconds(),
                func.unix_timestamp(models.Video.Time) < (event.TimeEnd-datetime(1970,1,1)).total_seconds())\
        .order_by(models.Video.Time)
    return jsonify({event.Name:event.dictionary(),
        'videos':[video.dictionary() for video in videos]})

if __name__ == '__main__':
    pass