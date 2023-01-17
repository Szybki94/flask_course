from flask import Flask, flash, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'  # <-- ale tak się nie robi, nie trzyma się tego bezpośrednio w apce


# CLASSES

class Currency:

    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return '<Currency {}>'.format(self.code)


class CantorOffer:

    def __init__(self):
        self.currencies = []
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'dolar.jpg'))
        self.currencies.append(Currency('EUR', 'Euro', 'euro.jpg'))
        self.currencies.append(Currency('JPY', 'Yen', 'NOT_IMPLEMENTED'))
        self.denied_codes.append('USD')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknow', 'unknow', 'pirate.jpg')


# FLASK APP

@app.route('/')
def index():
    return "This is index"


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    elif request.method == 'POST':
        currency = request.form['currency']
        if currency in offer.denied_codes:
            flash('The currency {}, CANNOT BE ACCEPTED'.format(currency))
        elif currency == "unknown":
            flash('The currency {}, CANNOT BE ACCEPTED'.format(currency))
        else:
            flash('The currency {} is ACCEPTABLE - request is OK'.format(currency))
        amount = request.form['amount']
        print(offer.get_by_code(currency))
        return render_template('exchange_results.html', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency))


if __name__ == "__main__":
    app.run(debug=True)
