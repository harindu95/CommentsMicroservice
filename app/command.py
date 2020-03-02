from app import events
from app.db.comment import Comment

def new_comment(userId, postId, body, parent_id):
    comment = Comment(userId, postId, body, parent_id=parent_id)
    event = events.newComment(comment)
    events.fireEvent(event)

def update_comment(commentId, userId, postId, body, parent_id):
    comment = Comment(userId, postId, body, id=commentId)
    event = events.updateComment(comment)
    events.fireEvent(event)

def delete_comment(commentId, userId, postId):
    comment = Comment(userId, postId, '' , id=commentId)
    event = events.deleteComment(comment)
    events.fireEvent(event)