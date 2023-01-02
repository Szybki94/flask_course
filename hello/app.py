from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return f'''<h1>Hello world</h1>
    and __name__ is: {__name__}'''
