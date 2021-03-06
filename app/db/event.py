from datetime import datetime
from flask import jsonify
from app.db.db import db
from app.db.comment import Comment

class Event(db.Model):
    '''Database Model Event class'''

    event_id = db.Column(db.Integer, primary_key = True)
    event_type = db.Column(db.String(100), nullable = False)
    event_created = db.Column(db.TIMESTAMP, default=True)
    comment_id = db.Column(db.Integer, nullable= True)
    post_id = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, nullable = False)
    created = db.Column(db.TIMESTAMP, default=True)
    body = db.Column(db.Text, nullable = True)
    parent_id = db.Column(db.Integer, nullable=True)
    
    
    def __init__(self , type , user_id, post_id, body = None, id = None, parent_id=None):
        self.event_type = type
        self.event_created = datetime.now()
        self.comment_id = id
        self.created = datetime.now()
        self.user_id = user_id
        self.post_id = post_id
        self.body = body
        self.parent_id = parent_id


    def serialize(self):
        '''Serialize object into a dictionary'''
        return dict({'id':self.id, 'created' : self.created, 'UserId':self.userId,
         'PostId' :self.postId,
         'Body': self.body, 'ParentId' :self.parent_id})
        

    def getComment(self):
        '''Convert data into a Comment'''
        return Comment(self.user_id, self.post_id, body = self.body,
         id = self.comment_id, parent_id=self.parent_id)