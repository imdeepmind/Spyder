from os import getenv
from flask import Flask

from db import db

app = Flask(__name__)

app.config['ENV'] = getenv("PYTHON_ENV")
app.config['DEBUG'] = getenv("FLASK_DEBUG")
app.config['TESTING'] = getenv("FLASK_TESTING")

@app.route('/', methods=["GET"])
def spyder_works():
    return 'Spyder Works!!!'