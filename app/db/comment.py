from datetime import datetime
from flask import jsonify

class Comment:

    def __init__(self ,userId, postId, body, id= None, parent_id=None):
        self.id = id
        self.created = datetime.now()
        self.userId = userId
        self.postId = postId
        self.body = body
        self.parent_id = parent_id

    def serialize(self):
        return dict({'id':self.id, 'created' : self.created, 'UserId':self.userId,
         'PostId' :self.postId,
         'Body': self.body, 'ParentId' :self.parent_id})
        
