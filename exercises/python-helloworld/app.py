from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlddd!"

@app.route("/status")
#def status():
    valu = {
        "user": "admin", "statuscode": "200"
    }
    return json.dumps(valu)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
