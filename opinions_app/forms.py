from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        [DataRequired('Обязательное поле'), Length(1, 128)]
    )
    text = TextAreaField(
        'Напишите мнение',
        [DataRequired('Обязательное поле')]
    )
    source = URLField(
        'Добавьте ссылку на подробный обзор фильма',
        [Length(1, 256), Optional()]
    )
    submit = SubmitField('Добавить')
