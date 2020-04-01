'''Query module designed according to CQRS architecture.
Handless all the queries from api. In contrast to the design document
We are handling the events in the same thread.
'''

from app.db.comment import Comment
import threading
from app.event_handler import check_events
from flask import current_app

def getComment(id):
    '''Retrieve a comment by id from database'''
    check_events()
    return Comment.query.filter_by(id = id).first()

def getCommentsUserId(user_id):
    '''Retrieve comments by user id from database'''
    check_events()
    return Comment.query.filter_by(user_id=user_id).all()

def getCommentsPostId(postId):
    '''Retrieve comments by post id from database'''
    check_events()
    return Comment.query.filter_by(post_id = postId).all()