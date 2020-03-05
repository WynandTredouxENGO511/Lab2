import os
import requests

from flask import Flask, session, request, render_template, redirect, url_for, abort, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# function to deal with quotes in SQL queries
def SQLquotes(str):
    if "'" in str:
        return str.replace("'", "''")
    else:
        return str

app = Flask(__name__)

# Load config
app.config.from_pyfile('config.cfg', silent=True)  # load settings from config.cfg
Session(app)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
