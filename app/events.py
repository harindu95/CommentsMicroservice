from app.db import db
from app import event_handler


def fireEvent(event):
    '''Store event in database.
    
    Args:
        event (Event) : Event to be stored in event store
    '''
    # store event
    database = db.get_db()
    database.session.add(event)
    database.session.commit()


