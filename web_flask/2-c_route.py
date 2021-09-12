#!/usr/bin/python3
""" Start Flask """
from flask import Flask, app

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB!!"""
    return "HBNB"


@app.route('/c/<phrase>', strict_slashes=False)
def c(phrase):
    """ C + Phrases!!! """
    return 'C {}'.format(phrase.replace('_', ' '))

if __name__ == "__main__":
    app.run()
