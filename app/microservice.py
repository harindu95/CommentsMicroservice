from flask import Flask,jsonify,request
import os
from app.db import db
from app.init import create_app
from app.db.comment import Comment
from app import command, query

app = create_app()
db.init_app(app)
query.setup(app)

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
    if comment is None:
        return jsonify({"status":"error", "message":"comment doesn't exist"}, 400)
    else:
        return comment.toJson()
   

@app.route("/api/comments/userId/<userId>")
def comments_by_user_id(userId):
    comments = query.getCommentsUserId(userId)
    response = []
    for comment in comments:
        response.append(comment.toJson())    

    return jsonify(response)

@app.route("/api/comments/postId/<postId>")
def comments_by_post_id(postId):
    comments = query.getCommentsPostId(postId)
    return jsonify([c.serialize() for c in comments])
    

@app.route("/api/comment/new", methods=["POST"])
def new_comment():
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    body = request.form["Body"]
    parentId = request.form["ParentId"]
    parentId = 0
    command.new_comment(userId, postId, body, parent_id = parentId)
    resp = jsonify(success=True)
    return resp

@app.route("/api/comment/update", methods=["POST"])
def update_comment():
    commentId = request.form["CommentId"]
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    body = request.form["Body"] 
    parentId = request.form["ParentId"]
    command.update_comment(commentId, userId, postId, body, parent_id = parentId)
    resp = jsonify(success=True)
    return resp


@app.route("/api/comment/delete", methods=["POST"])
def delete_comment():
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    commentId = request.form["CommentId"]
    command.delete_comment(commentId, userId, postId)
    resp = jsonify(success=True)
    return resp
