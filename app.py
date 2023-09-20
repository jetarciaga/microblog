import datetime
from flask import Flask, render_template, request

from database import Database

def create_app():
    app = Flask(__name__)
    db = Database()
    db.create_tables()

    @app.route("/", methods=["GET", "POST"])
    def home():

        if request.method == "POST":
            entry_content = request.form.get("content")
            db.add_entry(entry_content)

        db_entries = db.retrieve_entries()
        entries = []         
        for entry in db_entries:
            entries.append(
                [entry[1],
                entry[2],
                datetime.datetime.strftime(entry[2], "%b %d")
                ]
                )

        return render_template("home.html", entries=entries)
    return app