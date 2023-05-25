#!/usr/bin/env python3
"""Setup a basic Flask app and instantiate the Babel object in the app. Store
it in a module-level variable named babel"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """function to determine the best match with supported languages."""
    locale = request.args.get("locale")
    if locale is None:
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return locale


@app.route("/")
def home():
    """Function for home page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
