#!/usr/bin/python3
"""
Module starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays C followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """
    displays Python followed by the value of the text variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_numeral(n):
    """displays n is a number"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    """displays template if n is a number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_even_odd_template(n):
    """
    display HTML Page with Number: n is even|odd if n is an int
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
