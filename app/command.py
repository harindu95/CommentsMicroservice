from app import events
from app.db.comment import Comment

def new_comment(userId, postId, body):
    comment = Comment(userId, postId, body)
    event = events.newComment(comment)
    events.fireEvent(event)

def update_comment(commentId, userId, postId, body):
    comment = Comment(userId, postId, body, id=commentId)
    event = events.updateComment(comment)
    events.fireEvent(event)

def delete_comment(userId, postId, body):
    comment = Comment(userId, postId, body)
    event = events.deleteComment(comment)
    events.fireEvent(event)