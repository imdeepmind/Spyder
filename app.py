import re
from os import getenv
from flask import Flask, request, make_response
from time import strftime

from spyder import generate_web
from utils import logger, send_resp

app = Flask(__name__)

app.config['ENV'] = getenv("PYTHON_ENV")
app.config['DEBUG'] = getenv("FLASK_DEBUG")
app.config['TESTING'] = getenv("FLASK_TESTING")


@app.route('/', methods=["GET"])
def spyder_works():
    return make_response(send_resp(200, "Spyder Works!!!"), 200)

@app.route("/start", methods=["POST"])
def start_web():
    data = request.json

    if not "headstart" in data or not re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data["headstart"]):
        return make_response(send_resp(400, "Please provide a headstart"), 400)    
    
    generate_web(data["headstart"])

    return make_response(send_resp(200, "Started generating web"), 200)

@app.after_request
def after_request(response):
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.info('%s %s %s %s %s %s',
                    ts,
                    request.remote_addr,
                    request.method,
                    request.scheme,
                    request.full_path,
                    response.status)
    return response

@app.errorhandler(Exception)
def handle_error(error):
    logger.exception(error)
    return make_response(send_resp(500, "Something went wrong with the server"), 500)
