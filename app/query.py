from app.db import db
import threading
from app.event_handler import handle_event

event_thread = threading.Timer(10,handle_event)
event_thread.start()

def close_thread(e=None):
    event_thread.cancel()

def setup(app):
    app.teardown_appcontext(close_thread)

def getComment(id):
    return db.getComment(id)

def getCommentsUserId(userId):
    return db.getCommentsUserId(userId)

def getCommentsPostId(postId):
    return db.getCommentsPostId(postId)