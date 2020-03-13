from app import events
from app.db.event import Event

def new_comment(userId, postId, body, parent_id):
    event = Event("NEW COMMENT", userId, postId, body, parent_id=parent_id)
    events.fireEvent(event)

def update_comment(commentId, userId, postId, body, parent_id):
    event = Event("UPDATE COMMENT", userId, postId, body, parent_id=parent_id)
    events.fireEvent(event)

def delete_comment(commentId, userId, postId):
    event = Event("DELETE COMMENT", userId, postId)
    events.fireEvent(event)