from app.db import db

class Event:

    def __init__(self, type, comment):
        self.type = type
        self.comment = comment


def fireEvent(event):
    # store event
    db.storeEvent(event)


def newComment(comment):
    event = Event("NEW COMMENT", comment)
    return event

def updateComment(comment):
    event = Event("UPDATE COMMENT", comment)
    return event


def deleteComment(comment):
    event = Event("DELETE COMMENT", comment)
    return event
