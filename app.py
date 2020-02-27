import flask
import subprocess
import time
app = flask.Flask(__name__)
@app.route('/',methods=["POST"])
def todownload():
    if flask.request.method=="POST":
        localtime = time.asctime( time.localtime(time.time()) )
        with open("test.txt","w") as f:
            f.writelines(localtime)
    return localtime
if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port= 5050,
      debug=True
    )