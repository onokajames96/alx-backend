#!/usr/bin/env python3
""" Flask"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """Determines languages"""
    local_lang = request.args.get('locale')
    support_lang = app.config['LANGUAGES']
    if local_lang in support_lang:
        return local_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get user"""
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Get user before request"""
    g.user = get_user()


@app.route('/')
def index():
    """Returns template rendered"""
    return render_template("5-index.html")


if__name__ == "__main__":
    app.run()
