
from flask import Flask, request, jsonify
import os
import ssl


app = Flask(__name__)


CERTIFICATE_PATH = '/Users/sree/autozone/certs/cert.pem'
PRIVATE_KEY_PATH = '/Users/sree/autozone/certs/key.pem'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERTIFICATE_PATH, keyfile=PRIVATE_KEY_PATH)

@app.route("/", methods=["GET"])
def get_data():
    data = {
        "message": "Hello there!",
        "author": "Sree"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(ssl_context=context, host="0.0.0.0", port=8080)