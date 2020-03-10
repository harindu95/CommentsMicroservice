from app.db import db
import threading
from app import event_handler
from flask import current_app

event_thread = None

def close_thread(e=None):
    event_thread.stop()
    event_thread.join()

def setup(app):
    global event_thread
    # app.teardown_appcontext(close_thread)
    event_thread = event_handler.Thread(app)
    event_thread.start()
    # pass

def getComment(id):
    return db.getComment(id)

def getCommentsUserId(userId):
    return db.getCommentsUserId(userId)

def getCommentsPostId(postId):
    return db.getCommentsPostId(postId)