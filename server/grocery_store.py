import os

import requests
from flask import Flask

app = Flask(__name__)

def healthCheck():
    print("Checking healthCheck...")
    data = {"message": "The app is healthy"}
    return jsonify(data)


@app.route("/")
def welcome():
    return "Welcome to the grocery store !"


@app.route("/products")
def products():
    url = "{}".format(os.getenv("INVENTORY_URL"))
    resp = requests.get(url)
    return resp.text

@app.route("/health")
def health():
    return healthCheck()

if __name__ == "__main__":
    print("Grocery started, The inventory url is {}".format(os.getenv("INVENTORY_URL")))
    app.run(debug=True, host='0.0.0.0', port=5000)
