"""from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_data():
    data = {
        "message": "Hello there!",
        "author": "Sree"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)