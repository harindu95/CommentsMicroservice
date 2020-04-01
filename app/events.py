from app.db import db
from app import event_handler


def fireEvent(event):
    '''Store event in database.'''
    # store event
    database = db.get_db()
    database.session.add(event)
    database.session.commit()


