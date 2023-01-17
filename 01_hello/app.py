from flask import Flask, redirect,  request, url_for


app = Flask(__name__)


@app.route('/')
def index():

    menu = f'''
        <a href="{ url_for('exchange') }"> Currency exchange</a><br>
        <a href="{ url_for('cantor', currency='GBP', amount=50, _external=True) }">Exchange 50GBP</a><br>
        <img src="{ url_for('static', filename='apu_the_frog.jpg') }" height="300">
'''

    return menu


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
        elif currency == "0":
            return redirect(url_for('index'))
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
