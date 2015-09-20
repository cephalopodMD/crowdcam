__author__ = 'acl3qb'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from application import db
from sqlalchemy.sql import func
import time
from datetime import datetime

class Video(db.Model):

    __tablename__ = 'videos'
    VideoID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer)
    Time = db.Column(db.DateTime)
    Lat = db.Column(db.Float)
    Lng = db.Column(db.Float)
    Extension = db.Column(db.VARCHAR(8))

    def __init__(self, UserID, Time, Lat, Lng, Extension):
        self.UserID = UserID
        self.Time = Time
        self.Lat = Lat
        self.Lng = Lng
        self.Extension = Extension

    def dictionary(self):
        return {
            'id':self.VideoID,
            'datetime':self.Time,
            'lat':self.Lat,
            'lng':self.Lng,
            'extension':self.Extension
        }

class Event(db.Model):

    __tablename__ = 'events'
    EventID = db.Column(db.Integer, primary_key=True)
    TimeStart = db.Column(db.DateTime)
    TimeEnd = db.Column(db.DateTime)
    LatStart = db.Column(db.Float)
    LatEnd = db.Column(db.Float)
    LngStart = db.Column(db.Float)
    LngEnd = db.Column(db.Float)
    Name = db.Column(db.VARCHAR(32))

if __name__ == '__main__':
    pass