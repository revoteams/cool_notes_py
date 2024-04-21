"""Модуль содержит форму для создания/редактирования заметки"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class NoteForm(FlaskForm):
    """Форма для создания/редактирования заметки"""
    name = StringField('Название', validators=[
        DataRequired(),
        Length(1, 50, 'Длина названия должна быть от %(min)d до %(max)d символов.')
    ])
    content = TextAreaField('Текст', validators=[
        DataRequired(),
        Length(1, 1024, 'Размер заметки должен быть от %(min)d до %(max)d символов.')
    ])
