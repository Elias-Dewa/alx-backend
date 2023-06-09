#!/usr/bin/env python3
"""Setup a basic Flask app and instantiate the Babel object in the app. Store
it in a module-level variable named babel"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """a method returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed."""
    userId = request.args.get("login_as")
    if userId:
        return users.get(int(userId))


@app.before_request
def before_request():
    """a method to find a user if any"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """function to determine the best match with supported languages."""
    locale = request.args.get("locale")
    if locale:
        if locale in Config.LANGUAGES:
            return locale
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in Config.LANGUAGES:
            return locale
    locale = request.headers.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """Function for home page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
