"""This module handles flask routing and json endpoints"""

from flask import Flask,jsonify,request
import os
from app.init import create_app
from app.db import db
from app.db.comment import Comment
from app import command, query
from app.validation import *
from schema import SchemaError
from app.logging import log

app = create_app()
log.info("Application initialized")

db.init_app(app)
log.info("Connected to database")

@app.route("/")
def main():
    """ Basic root endpoint. Not used within application"""
    return "Welcome !!"

# Need to setup mysql beforehand
@app.route("/database")
def db_test():
    """Basic endpoint used to test the database connection"""
    d = db.get_db()    
    return "Database connected"

@app.route("/api/comment/id/<id>/")
def comment(id):
    """Retrieve Comment using CommentID
    
      Args: 
        id (int): comment id

      Return:
        comment: a JSON representation of Comment
    """
    response = {}
    try:
        commentIdSchema.validate(id)
        comment = query.getComment(id)
        if comment is None :
            return jsonify({"status":"error", "message":"comment doesn't exist"}, 400)
        else:
            return jsonify(comment.serialize())

    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
        return resp

@app.route("/api/comments/userId/<userId>")
def comments_by_user_id(userId):
    """Retrieve multiple comments by UserID
    
     Args: 
        userId (int): user id of comments

      Return:
        comments: a JSON representation of a list of Comments
    """
    response = []
    try:
        userIdSchema.validate(userId)
        comments = query.getCommentsUserId(userId)
        
        if not comments :
            return jsonify({"status":"error", "message":"no comments posted by user"}, 400)
        else:
            return jsonify([c.serialize() for c in comments])

    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
        return resp

@app.route("/api/comments/postId/<postId>")
def comments_by_post_id(postId):
    '''Retrieve multiple comments by post id
    
     Args: 
        postId (int): comment id

      Return:
        comments: a JSON representation of a list of Comments
    '''
    try:
        postIdSchema.validate(postId)
        comments = query.getCommentsPostId(postId)
        if not comments :
            return jsonify({"status":"error", "message":"no comments posted under post"}, 400)
        else:
            return jsonify([c.serialize() for c in comments])
        
    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
        return resp
    

@app.route("/api/comment/new", methods=["POST"])
def new_comment():
    """Create a new comment using POST request.

     Args: 
        UserId (int): user id
        PostId (int): post id
        Body   (str): comment text
        ParentId (int): Parent comment id

      Return:
        success = True or error message
    """
    data = request.form.to_dict()
    try:
        data = newCommentSchema.validate(data)
        userId = data["UserId"]
        postId = data["PostId"]
        body = data["Body"]
        parentId = data["ParentId"]
        command.new_comment(userId, postId, body, parent_id = parentId)
        resp = jsonify(success=True)
    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
    return resp


@app.route("/api/comment/update", methods=["POST"])
def update_comment():
    """Update an existing comment with POST request. Return an error 
    message if comment doesn't exist
    
    Args: 
        CommentId (int) : comment id
        UserId (int): user id
        PostId (int): post id
        Body   (str): comment text
        ParentId (int): Parent comment id

      Return:
        success = True or error message
    """
    data = request.form.to_dict()
    try:        
        data = updateCommentSchema.validate(data)
        userId = data["UserId"]
        postId = data["PostId"]
        body = data["Body"]
        parentId = data["ParentId"]   
        commentId = data["CommentId"]
        result = command.update_comment(commentId, userId, postId, body, parent_id = parentId)
        if result :     
            resp = jsonify(success=True)   
        else:
            resp = jsonify(error="Comment doesn't exist")
    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
    return resp


@app.route("/api/comment/delete", methods=["POST"])
def delete_comment():
    """Delete an existing comment using POST request. Return an error 
    message if comment doesn't exist
    
      Args: 
        CommentId (int) : comment id
       
      Return:
        success = True or error message
    """
    data = request.form.to_dict()
    try:        
        data = deleteCommentSchema.validate(data)         
        commentId = data["CommentId"]
        result = command.delete_comment(commentId) 
        if result :     
            resp = jsonify(success=True)   
        else:
            resp = jsonify(error="Comment doesn't exist")

    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
        log.error("Exception occurred", exc_info=True)
    return resp
