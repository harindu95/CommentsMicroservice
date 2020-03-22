from app.db import db
from app import event_handler

class Event:

    def __init__(self, type, comment):
        self.type = type
        self.comment = comment


def fireEvent(event):
    # store event
    database = db.get_db()
    database.session.add(event)
    database.session.commit()


