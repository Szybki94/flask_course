from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return f'''<h1>Hello world</h1>
    and __name__ is: {__name__}'''

@app.route('/about')
def about():
    return "Flask programming time!!!"


if __name__ == "__main__":
    app.run(debug=True)
