__author__ = 'acl3qb'

from flask import Flask, send_file
from . import app

@app.route('/doc')
def doc():
    return send_file('apis/index.html')