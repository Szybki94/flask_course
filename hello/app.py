from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():

    color = "black"
    style = "normal"
    if 'color' in request.args:
        color = request.args['color']
    if 'style' in request.args:
        style = request.args['style']
    print(color, style)
    return f'''<h1 style="color: {color};font-style: {style};">Hello world</h1>
    and __name__ is: {__name__}'''


@app.route('/about')
def about():
    return "Flask programming time!!!"


@app.route('/cantor/<string:currency>/<int:amount>/')
def cantor(currency, amount):
    return "{} - {}".format(currency, amount)





if __name__ == "__main__":
    app.run(debug=True)
