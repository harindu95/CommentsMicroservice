from app.db.comment import Comment
import threading
from app.event_handler import check_events
from flask import current_app

def getComment(id):
    check_events()
    return Comment.query.filter_by(id = id).first()

def getCommentsUserId(user_id):
    check_events()
    return Comment.query.filter_by(user_id=user_id).all()

def getCommentsPostId(postId):
    check_events()
    return Comment.query.filter_by(post_id = postId).all()