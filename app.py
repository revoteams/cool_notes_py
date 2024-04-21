"""Главный модуль, запускающий приложение"""

import webbrowser
from os import getenv
from flask import Flask, render_template
from dotenv import load_dotenv
from models.db import db
from models.note import Note
from routes.notes import notes

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + getenv("SQLITE_DB_FILE")
db.init_app(app)

app.register_blueprint(notes, url_prefix="/notes")

with app.app_context():
    db.create_all()

@app.route("/")
def start_page():
    """Главная страница"""
    notes_list = db.session.execute(
        db.select(Note)
    ).scalars()
    return render_template('notes_catalog.html', notes=notes_list)

@app.errorhandler(404)
def page_not_found(error):
    """Заметка или страница не найдена"""
    return render_template('404.html', error=error), 404

if getenv("OPEN_BROWSER"):
    webbrowser.open('http://127.0.0.1:8080')
