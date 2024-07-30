#!/usr/bin/python3
"""
starts a Flask web application that listens
on 0.0.0.0 port 5000
"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    """Return an HTML Page that displays the list of cities"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(excep):
    """Call storage.close function"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
