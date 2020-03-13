from datetime import datetime
from flask import jsonify
from app.db.db import db

# db = database.get_db()

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable = False)
    user_name = db.Column(db.String(100), nullable = False)
    created = db.Column(db.TIMESTAMP, default=True)
    body = db.Column(db.Text, nullable = False)
    parent_id = db.Column(db.Integer, nullable=True)
    
    def __init__(self ,user_name, post_id, body, id = None, parent_id=None):
        self.id = id
        self.created = datetime.now()
        self.user_name = user_name
        self.post_id = post_id
        self.body = body
        self.parent_id = parent_id

    def serialize(self):
        return dict({'id':self.id, 'created' : self.created, 'user_name':self.user_name,
         'post_id': self.post_id,
         'body': self.body, 'parent_id' :self.parent_id})
        
