from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worldd!"

@app.route("/status")
def status():
    value = {
        "user": "admin", "statuscode": "200"
    }
    return json.dumps(value)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
