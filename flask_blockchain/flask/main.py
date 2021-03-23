from flask import *
from block import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        write_block(name=lender, amount=amount, to_whom=borrower)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
