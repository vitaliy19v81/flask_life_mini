from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import NumberRange


class SizeForm(FlaskForm):
    width = IntegerField('Ширина мира', validators=[NumberRange(min=10, max=30)])
    height = IntegerField('Высота мира', validators=[NumberRange(min=10, max=30)])
    submit = SubmitField('принять')
