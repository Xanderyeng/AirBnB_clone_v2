#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """
    method for say hello
    Returns:
        [str]: "Hello HBNB!"
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
