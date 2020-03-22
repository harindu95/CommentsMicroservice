from flask import Flask,jsonify,request
import os
from app.init import create_app
from app.db import db
from app.db.comment import Comment
from app import command, query
from app.validation import *
from schema import SchemaError

app = create_app()
db.init_app(app)


@app.route("/")
def main():
    return "Welcome !!"

# Need to setup mysql beforehand
@app.route("/database")
def db_test():
    d = db.get_db()
    return "Database connected"

@app.route("/api/comment/id/<id>/")
def comment(id):
    response = {}
    comment = query.getComment(id)
    if comment is None :
        return jsonify({"status":"error", "message":"comment doesn't exist"}, 400)
    else:
        return jsonify(comment.serialize())


@app.route("/api/comments/userId/<userId>")
def comments_by_user_id(userId):
    comments = query.getCommentsUserId(userId)
    response = []
    if not comments :
        return jsonify({"status":"error", "message":"no comments posted by user"}, 400)
    else:
        return jsonify([c.serialize() for c in comments])


@app.route("/api/comments/postId/<postId>")
def comments_by_post_id(postId):
    comments = query.getCommentsPostId(postId)
    if not comments :
        return jsonify({"status":"error", "message":"no comments posted under post"}, 400)
    else:
        return jsonify([c.serialize() for c in comments])
        

    

@app.route("/api/comment/new", methods=["POST"])
def new_comment():
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
    return resp

# def validate_commentId(self, commentId):
#         if ceil(commentId) != commentId
#             raise ValidationError('Comment Id must be numerical only.')
# def validate_bodyLength(self, body):
#     length = SELECT LEN(body);
#         if length > 140
#             raise ValidationError('Comment is too long.')


@app.route("/api/comment/update", methods=["POST"])
def update_comment():
    data = request.form.to_dict()
    try:        
        data = updateCommentSchema.validate(data)
        userId = data["UserId"]
        postId = data["PostId"]
        body = data["Body"]
        parentId = data["ParentId"]   
        commentId = data["CommentId"]
        command.update_comment(commentId, userId, postId, body, parent_id = parentId)
        resp = jsonify(success=True)
    except SchemaError as e:
        resp = jsonify(error=schema_message(e))
    return resp

# def validate_postId(self, postId):
#         if ceil(postId) != postId
#             raise ValidationError('Post Id must be numerical only.')
# def validate_commentId(self, commentId):
#         if ceil(commentId) != commentId
#             raise ValidationError('Comment Id must be numerical only.')
# def validate_bodyLength(self, body):
#     length = SELECT LEN(body);
#         if length > 140
#             raise ValidationError('Comment is too long.')

@app.route("/api/comment/delete", methods=["POST"])
def delete_comment():
    data = request.form.to_dict()
    try:        
        data = deleteCommentSchema.validate(data)
        userId = data["UserId"]
        postId = data["PostId"]       
        commentId = data["CommentId"]
        command.delete_comment(commentId, userId, postId)       
        resp = jsonify(success=True)   

    except SchemaError as e:
        print(e.autos)
        resp = jsonify(error=schema_message(e))

    return resp

# def validate_postId(self, postId):
#         if ceil(postId) != postId
#             raise ValidationError('Post Id must be numerical only.')
# def validate_commentId(self, commentId):
#         if ceil(commentId) != commentId
#             raise ValidationError('Comment Id must be numerical only.')
