from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
    <!doctype html>
    <title>CrowdCam</title>
    <h1>Document the world together</h1>
    '''
