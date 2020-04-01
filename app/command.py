'''Command module designed according to CQRS architecture.
Handless all the commands(changes to database) from api. 
'''

from app import events
from app.db.event import Event
from app.db.comment import Comment

def new_comment(userId, postId, body, parent_id):
    ''' Create new comment
     
    Args: 
        commentId (int) : comment id
        userId (int): user id
        postId (int): post id
        body   (str): comment text
        parent_id (int): Parent comment id
    '''
    event = Event("NEW COMMENT", userId, postId, body, parent_id=parent_id)
    events.fireEvent(event)

def update_comment(commentId, userId, postId, body, parent_id):
    '''Update existing comment. Return True if the comment exists. False otherwise.
    
    Args: 
        commentId (int) : comment id
        userId (int): user id
        postId (int): post id
        body   (str): comment text
        parent_id (int): Parent comment id

      Return:
       True if comment exists, False if not.
    '''
    c = Comment.query.filter_by(id = commentId).first()
    if c == None:
        return False
    else:
        event = Event("UPDATE COMMENT", userId, postId, body,id=commentId, parent_id=parent_id)
        events.fireEvent(event) 
        return True

def delete_comment(commentId):
    '''Delete existing comment. Return True if the comment exists. False otherwise
    
    Args: 
        commentId (int) : comment id

    Return:
       True if comment exists, False if not.
    '''
    c = Comment.query.filter_by(id = commentId).first()
    if c == None:
        return False

    else:
        event = Event("DELETE COMMENT", 0, 0, id=commentId)
        events.fireEvent(event)
        return True
