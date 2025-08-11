# Flask & DB


import sqlite3

import flask
from flask import Flask


def run8():
    app = flask.Flask(__name__)

    @app.route('/')
    def home():
        return "Hello world"

    app.run()
