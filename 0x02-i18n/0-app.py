#!/usr/bin/env python3
"""
flask application
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Rendering template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
