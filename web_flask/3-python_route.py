#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Hello Hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Hello hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_compliment(text):
    """ Displaying a message starting with C """
    msg = text.replace('_', ' ')
    return 'C %s' % msg


@app.route('/python/')
@app.route('/python/<text>')
def python_compliment(text='is_cool'):
    """ Displaying a message starting with Python """
    msg = text.replace('_', ' ')
    return 'Python %s' % msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
