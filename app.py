from flask import Flask, render_template, request

from CurrencyConv import Conv
from PiCalc import compute
from PiCalc import PiCalc
from model import InputForm
from model import CurrForm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/picalc')
def picalc():
    return render_template('PiCalc.html')


@app.route("/computeResult", methods=['GET', 'POST'])
def computeResult():
    form = InputForm(request.form)
    numTerms = 0
    approximation = 0
    if request.method == 'POST' and form.validate():
        result = compute(form.decimalPlaces.data, form.speed.data)
        obj = PiCalc(int(form.decimalPlaces.data))
        numTerms = 0
        approximation = 0
        if (form.speed.data == "Fast"):
            numTerms = obj.getNumberTermsMachinApprox()
            print(numTerms)
            approximation = obj.fast_pi_approximation()
            print(approximation)
        else:
            numTerms = obj.getNumberTermsSlowApprox()
            print(numTerms)
            approximation = obj.calculation_slow_approx()
            print(approximation)
    else:
        result = None
    return render_template("PiCalc.html", form=form, result=result, numTerms=numTerms, approximation=approximation)


@app.route("/CurrencyConv")
def currConv():
    return render_template("CurrencyConv.html")


@app.route("/computeConv", methods=['GET', 'POST'])
def computeConv():
    form = CurrForm(request.form)
    baseCurr = form.baseCurr.data
    targetCurr = form.targetCurr.data
    amount = form.baseCurrAmount.data
    obj = Conv(baseCurr, targetCurr, amount)
    resultAmount = obj.urlResponse()
    my_string = '{:,.2f}'.format(resultAmount)
    return render_template("CurrencyConv.html", form=form,  baseCurrAmount=amount, baseCurr=baseCurr,
                           targetValue=my_string, targetCurr=targetCurr)


@app.route("/monteCarlo")
def monteCarlo():
    return render_template("PiApproxMonteCarlo.html")


if __name__ == '__main__':
    app.run(debug=True)
