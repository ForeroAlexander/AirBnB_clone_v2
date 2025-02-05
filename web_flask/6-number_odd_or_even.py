  
#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Hello HBNB!!! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ HBNB!!! """
    return "HBNB"


@app.route('/c/<phrase>', strict_slashes=False)
def c(phrase):
    """ C + Phrases!!! """
    return 'C {}'.format(phrase.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<phrase>', strict_slashes=False)
def python(phrase='is cool'):
    """ Python + phrases!!!(is cool by default) """
    return 'Python {}'.format(phrase.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def number(num):
    """ It's a number! """
    if type(num) == int:
        return ("{} is a number".format(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def display_html(num):
    """ Display a HTML page. """
    if type(num) == int:
        return render_template('5-number.html', n=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def odd_or_even(num):
    """ Odd od Even Number """
    if type(num) == int:
        return render_template('6-number_odd_or_even.html', n=num)


if __name__ == '__main__':
    app.run()
