from app.db import db
from app import event_handler

class Event:

    def __init__(self, type, comment):
        self.type = type
        self.comment = comment


def fireEvent(event):
    # store event
    db.storeEvent(event)
    event_handler.event_buffer.append(event)


def newComment(comment):
    event = Event("NEW COMMENT", comment)
    return event

def updateComment(comment):
    event = Event("UPDATE COMMENT", comment)
    return event


def deleteComment(comment):
    event = Event("DELETE COMMENT", comment)
    return event
