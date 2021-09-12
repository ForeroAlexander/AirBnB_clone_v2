#!/usr/bin/python3
""" Start Flask """
from flask import Flask, app

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
