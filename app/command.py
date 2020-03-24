from app import events
from app.db.event import Event
from app.db.comment import Comment

def new_comment(userId, postId, body, parent_id):
    event = Event("NEW COMMENT", userId, postId, body, parent_id=parent_id)
    events.fireEvent(event)

def update_comment(commentId, userId, postId, body, parent_id):
    c = Comment.query.filter_by(id = commentId).first()
    if c == None:
        return False
    else:
        event = Event("UPDATE COMMENT", userId, postId, body,id=commentId, parent_id=parent_id)
        events.fireEvent(event) 
        return True

def delete_comment(commentId):
    c = Comment.query.filter_by(id = commentId).first()
    if c == None:
        return False

    else:
        event = Event("DELETE COMMENT", 0, 0, id=commentId)
        events.fireEvent(event)
        return True
