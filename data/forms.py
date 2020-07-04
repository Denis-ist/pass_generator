from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, NumberRange


class Passwords(FlaskForm):
    length = IntegerRangeField('Длина пароля:', validators=[DataRequired(), NumberRange(min=6, max=32)], default=6)
    count = IntegerRangeField('Количество паролей:', validators=[DataRequired(),NumberRange(min=4, max=32)], default=4)
