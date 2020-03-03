from app.db import db
import time

event_buffer = []

def handle_event():
    while(len(event_buffer) > 0):
        e = event_buffer.pop()
        if e.type == 'NEW COMMENT':
            db.insertComment(e.comment)
        elif e.type == 'UPDATE COMMENT':
            db.updateComment(e.comment)
        elif e.type == 'DELETE COMMENT':
            db.deleteComment(e.comment)
        else:
            print("invalid event type")