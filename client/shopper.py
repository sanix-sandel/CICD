#! /usr/bin/env python3
import json
import os
import time

# from common import configure_tracer, log, Log
import requests
from flask import Flask, jsonify

app = Flask(__name__)


def healthCheck():
    print("Checking healthCheck...")
    data = {"message": "The app is healthy"}
    return jsonify(data)


def browse():
    url = "{}/products".format(os.getenv("GROCERY_URL"))
    print("The url is {}".format(url))
    try:
        resp = requests.get(url)
        data = json.loads(resp.content)
        return add_item_to_cart(data)
    except Exception as err:
        print(err)


def add_item_to_cart(data):
    print("add {} to cart".format(data))
    return jsonify(data)


@app.route("/")
def visit_store():
    print("Visiting the grocery")
    return browse()


@app.route("/health")
def health():
    return healthCheck()



if __name__ == "__main__":
    print("Shopper is starting...")
    time.sleep(5)
    print("Shopper started, The grocery url is {}".format(os.getenv("GROCERY_URL")))
    app.run(debug=True, host='0.0.0.0', port=5555)
