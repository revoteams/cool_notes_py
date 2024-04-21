"""Модуль для работы SQLAlchemy в разных модулях"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Декларативная база"""

db = SQLAlchemy(model_class=Base)
