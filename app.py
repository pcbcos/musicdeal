import flask
from os import system
import time
app = flask.Flask(__name__)
@app.route('/',methods=["POST"])
def todownload():
    if flask.request.method=="POST":
        system("python3 test.py")
        localtime = time.asctime( time.localtime(time.time()) )
        with open("test.txt","w") as f:
            f.writelines(localtime)
    return localtime