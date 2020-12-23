import requests
from config import api_key


class Conv:

    # constructor (self.___ in python = this.___ in java)
    def __init__(self, baseCurrency, targetCurrency, amount):
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.amount = amount

    def getBaseCurrency(self):
        return self.baseCurrency

    def getTargetCurrency(self):
        return self.targetCurrency

    def getAmount(self):
        return self.amount

    def urlRequest(self):
        url = "http://data.fixer.io/api/latest?access_key={}".format(api_key)
        return url

    def urlResponse(self):
        url = self.urlRequest()
        response = requests.get(url)
        file = response.json()
        euroValue = 0

        targetValue = 0
        for currency, val in file['rates'].items():
            if currency == self.baseCurrency:
                euroValue = float(self.amount) / val
                break
        print(euroValue)

        for currency, val in file['rates'].items():
            if currency == self.targetCurrency:
                targetValue = euroValue * val
                break
        print(targetValue)
        return targetValue


obj = Conv('USD', 'JPY', 100)
print(obj.urlResponse())


def getWorldCurrencies():
    url = "http://data.fixer.io/api/symbols?access_key={}".format(api_key)
    response = requests.get(url)
    file = response.json()
    return file['symbols'].items()


def getFinalWorldCurrencies():
    url = "http://data.fixer.io/api/symbols?access_key={}".format(api_key)
    response = requests.get(url)
    file = response.json()
    currencies = []
    for key, val in file['symbols'].items():
        currencies.append((key, val))
    return currencies

