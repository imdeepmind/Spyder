from flask import Flask

app = Flask(__name__)

@app.route('/')
def spyder_works():
    return 'Spyder Works!!!'