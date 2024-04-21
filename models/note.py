"""Модуль содержит модель бд заметки"""
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.db import db

class Note(db.Model):
    """Модель заметки"""
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(String(1024))
    updated_at: Mapped[datetime] = mapped_column()
