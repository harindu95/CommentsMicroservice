from app.db import db
import threading
from app import event_handler

event_thread = event_handler.Thread()
event_thread.start()

def close_thread(e=None):
    event_thread.stop()
    event_thread.join()

def setup(app):
    app.teardown_appcontext(close_thread)

def getComment(id):
    return db.getComment(id)

def getCommentsUserId(userId):
    return db.getCommentsUserId(userId)

def getCommentsPostId(postId):
    return db.getCommentsPostId(postId)