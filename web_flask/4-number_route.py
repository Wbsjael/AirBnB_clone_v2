#!/usr/bin/python3
"""
modue that starts a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def index():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays c then value of text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """displays python then value of text variable"""
    return 'python ' + text.repace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_numeral(n):
    """displays n is a number"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
