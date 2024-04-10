#!/usr/bin/env python3
"""
Flask
"""
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best-matched language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Returns Current language"""
    return "Current language: {}".format(get_locale())


if __name__ == '__main__':
    app.run(debug=True)
