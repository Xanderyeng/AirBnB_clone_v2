#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    method for say hello
    Returns:
        [str]: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hello_hbnb():
    """
    method return HBNB
    Returns:
        [str]: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    method for say C is
    Returns:
        [str]: "c and the value of text"
    """
    return "C %s" % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    """
    method for say python is
    Returns:
        [str]: "python and the value of text"
    """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    method for say is a number
    Returns:
        [str]: "n is a number"
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    method for show html number
    Returns:
        "render of html"
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    method for show html odd or even
    Returns:
        "render of html for odd or even"
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
