
Lesson 2:
Architecture Consideration for Cloud Native Applications
 1. Introduction
 2. Design Considerations for Cloud-Native Applications
 3. Monoliths and Microservices
 4. Quizzes: Monoliths and Microservices
 5. Trade-offs for Monoliths and Microservices
 6. Quizzes: Trade-offs for Monoliths and Microservices
 7. Exercise: Trade-offs for Monoliths and Microservices
 8. Solution: Monoliths and Microservices
 9. Best Practices For Application Deployment
 10. Quizzes: Best Practices For Application Deployment
 11. Exercise: Endpoints for Application Status
 12. Solution: Endpoints for Application Status
 13. Exercise: Application Logging
 14. Solution: Application Logging
 15. Edge Case: Amorphous Applications
 16. Lesson Conclusion
Solution: Endpoints for Application Status
Solution: Endpoints for Application Status

The following snippet showcases an example of a Python Flask application, with /metrics, /status and main page (/) endpoints:

from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
;
