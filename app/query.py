from app.db.comment import Comment
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
    return Comment.query.filter_by(id = id).first()

def getCommentsUserId(user_id):
    return Comment.query.filter_by(user_id=user_id).all()

def getCommentsPostId(postId):
    return Comment.query.filter_by(post_id = postId).all()