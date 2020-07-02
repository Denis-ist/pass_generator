from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SubmitField
from wtforms.validators import DataRequired


class Passwords(FlaskForm):
    length = IntegerField('Длина пароля:', validators=[DataRequired()])
    count = IntegerField('Количество паролей:', validators=[DataRequired()])
    submit = SubmitField('Сгенерировать', validators=[DataRequired()])