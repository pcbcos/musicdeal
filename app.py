import flask
import subprocess
import time
app = flask.Flask(__name__)
@app.route('/')
def todownload():
    localtime = time.asctime( time.localtime(time.time()) )
    with open("test.txt","w") as f:
        f.writelines(localtime)
    return localtime
