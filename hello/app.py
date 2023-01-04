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


@app.route('/exchange', methods=["GET", "POST"])
def exchange():

    body = '''
    <form id="exchange_form" action="" method="POST">
        <label for="currency">Currency</label>
        <input type="text" id="currency" name="currency" value="EUR"><br>
        <label for="amount">Amount:</label>
        <input type="text" id="amount" name="amount" value="100"><br>
        <input type="submit" value="Zatwierdź">
    </form>'''

    if request.method == "GET":
        return body

    elif request.method == "POST":
        currency = request.form["currency"] or None
        amount = request.form["amount"] or None
        if not currency or not amount:
            return "Please send proper form"
        return f"{currency} - {amount}"


# @app.route('/exchange-proceed', methods=["POST"])
# def exchange_proceed():
#     if request.method == "POST":
#         currency = request.form["currency"] or None
#         amount = request.form["amount"] or None
#         if not currency or not amount:
#             return "Please send proper form"
#         return f"{currency} - {amount}"


if __name__ == "__main__":
    app.run(debug=True)
