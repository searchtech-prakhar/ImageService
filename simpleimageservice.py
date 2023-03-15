#!/usr/bin/python3

import os
from time import sleep

from flask import Flask
from flask import request
from flask import jsonify

# Demo Imports
from Imagekit.lib import Image
from Imagekit.processors.resize import ResizeToFit
import requests
from io import BytesIO

# Set the version of the Flask Server
VERSION = "0.1"
if os.getenv("VERSION") is not None:
    VERSION = os.getenv("VERSION")

# Set the port to listen on
PORT = 9876
if os.getenv("PORT0") is not None:
    PORT = os.getenv("PORT0")

# Set the HEALTH_DELAY
HEALTH_DELAY = 0
if os.getenv("HEALTH_DELAY") is not None:
    HEALTH_DELAY = os.getenv("HEALTH_DELAY")

app = Flask(__name__)


@app.route("/env")
def captain_planet():
    settings = {}
    settings["version"] = VERSION
    settings["env"] = {}
    settings["env"] = dict(os.environ)
    return jsonify(settings)


## Health Status - /health
@app.route("/health")
def health():
    healthzee = {}
    healthzee["healthy"] = True
    healthzee["version"] = VERSION
    healthzee["delay in seconds"] = HEALTH_DELAY
    sleep(HEALTH_DELAY)  # wait this long in seconds
    return jsonify(healthzee)


## Info - /info
@app.route("/info")
def info():
    deepdive = {}
    deepdive["from"] = request.remote_addr  # the IP address of the requestor
    deepdive["host"] = request.host  # the IP:port of the flask server
    deepdive["version"] = VERSION
    return jsonify(deepdive)

@app.route('/resize', methods=["POST"])
def resize():

    url = request.json['url']
    print(f"\n Recived request for url {url}")
    r = requests.get(url)
    img = Image.open(BytesIO(r.content))
    img.show()
    # DP Small then resize it to fit within a 58x100 canvas.
    dp_small = ResizeToFit(200, 100).process(img)
    dp_small.show()
    response = {}
    response["from"] = request.remote_addr  # the IP address of the requestor
    response["host"] = request.host  # the IP:port of the flask server
    response["size"] = 200
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)