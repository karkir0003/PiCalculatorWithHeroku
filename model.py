from wtforms import Form, IntegerField, SelectField, validators
from math import pi

from CurrencyConv import getWorldCurrencies, getFinalWorldCurrencies


class InputForm(Form):
    style = {"style": "text-align:center"}
    decimalPlaces = SelectField(
        label='Select Decimal Approximation:', default=1,
        validators=[validators.InputRequired()],
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], render_kw=style
    )
    speed = SelectField(label="Select Approximation Speed:", validators=[validators.InputRequired()],
                        choices=[('Slow', 'Slow'), ('Fast', 'Fast')],
                        )


class CurrForm(Form):
    style = {"style": "text-align:center"}
    baseCurr = SelectField(
        label='Select Base Currency:', default='USD', validators=[validators.InputRequired()],
        choices=getFinalWorldCurrencies(), render_kw=style
    )

    baseCurrAmount = IntegerField(
        label='Enter Base Amount:', default='1', validators=[validators.NumberRange(min=1), validators.InputRequired()],
        render_kw=style
    )

    targetCurr = SelectField(
        label='Select Target Currency:', default='USD', validators=[validators.InputRequired()],
        choices=getFinalWorldCurrencies(), render_kw=style
    )
