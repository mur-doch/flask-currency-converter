from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import NumberInput
from app.helpers import get_currencies


class ConvertForm(FlaskForm):
    currency_one = SelectField('First Currency', choices=get_currencies())
    currency_two = SelectField('Second Currency', choices=get_currencies())
    amount_one = FloatField('First Amount', widget=NumberInput())
    amount_two = FloatField('Second Amount', widget=NumberInput())
    submit = SubmitField('Convert')
