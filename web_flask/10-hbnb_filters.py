#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0 port 5000
"""


from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def index():
    """Displays a HTML Page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(excep):
    """Call storage.close method"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
