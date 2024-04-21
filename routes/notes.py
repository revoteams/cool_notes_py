"""Пути связанные с CRUD заметки"""
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_
from models.db import db
from models.note import Note
from forms.note_form import NoteForm

notes = Blueprint('notes', __name__,
                        template_folder='templates')

@notes.route("/view/<int:note_id>")
def show_note(note_id):
    """Показ страницы заметки"""
    note = db.get_or_404(Note, note_id)
    return render_template("note_detail.html", note=note)

@notes.route("/search", methods=['POST', 'GET'])
def search_note():
    """Поиск заметки по request значению и вывод результатов"""
    if not request.form or not request.form["search"]:
        #Если при поиске вводят пустую строку
        return redirect(url_for('start_page'))
    search_str = request.form["search"]
    notes_list = db.session.execute(
        db.select(Note)
        .where(or_(Note.name.contains(search_str), Note.content.contains(search_str)))
    ).scalars()
    return render_template('notes_catalog.html', notes=notes_list)

@notes.route("/edit/<int:note_id>", methods=['POST', 'GET'])
def edit_note(note_id):
    """Показ страницы редактирования заметки"""
    note = db.get_or_404(Note, note_id)
    form = NoteForm()
    if form.validate_on_submit():
        #Обновление объекта заметки
        note.name=form.name.data
        note.content=form.content.data
        note.updated_at=datetime.now()
        db.session.commit()
        return redirect(url_for("notes.show_note", note_id=note.id))
    form.name.data = note.name
    form.content.data = note.content
    return render_template("note_form.html", form=form, edit_note=True, note_id=note.id)

@notes.route("/delete/<int:note_id>", methods=['POST'])
def delete_note(note_id):
    """Удаление заметки"""
    note = db.get_or_404(Note, note_id)

    if request.method == "POST":
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for("start_page"))

    return render_template("note_detail.html", note=note)

@notes.route("/create", methods=['POST', 'GET'])
def create_note():
    """Страница создания заметки"""
    form = NoteForm()
    if form.validate_on_submit():
        #Добавление объекта заметки
        note = Note(
            name=form.name.data,
            content=form.content.data,
            updated_at=datetime.now()
        )
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("notes.show_note", note_id=note.id))
    return render_template("note_form.html", form=form)
