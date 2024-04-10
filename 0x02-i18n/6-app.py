#!/usr/bin/env python3
"""Flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@app.route('/')
def index():
    """returns the template"""
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """ get locale"""
    url_lang = request.args.get('locale')
    if url_lang in app.config['LANGUAGES']:
        return url_lang
    user_lang = users[int(request.args.get('login_as'))]['locale']
    if request.args.get('login_as') else None

    if user_lang in app.config['LANGUAGES']:
        return user_lang
    header_lang = request.headers.get('locale')
    if header_lang in app.config['LANGUAGES']:
        return header_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """get user"""
    try:
        return users[int(request.args.get('login_as'))]
    except Exception:
        return None


@app.before_request
def before_request():
    """ get user before"""
    g.user = get_user()


if __name__ == "__main__":
    app.run()
