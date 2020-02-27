from flask import Flask,jsonify,request
import os
from app.db import db
from app.init import create_app

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
    response['type'] = 'Comment'
    response['id'] = id
    response['UserId'] = '213344'
    response['PostId'] = '213344'
    response['Body'] = 'Comment description'
    return jsonify(response)


@app.route("/api/comments/userId/<userId>")
def comments_by_user_id(userId):
    response = {}
    response['type'] = 'Comment'
    response['id'] = 1232
    response['UserId'] = userId
    response['PostId'] = '213344'
    response['Body'] = 'Comment description'
    return jsonify(response)

@app.route("/api/comments/postId/<postId>")
def comments_by_post_id(postId):
    response = {}
    response['type'] = 'Comment'
    response['CommentId'] = '1232'
    response['UserId'] = '23424'
    response['PostId'] = postId
    response['Body'] = 'Comment description'
    return jsonify(response)


@app.route("/api/comment/new", methods=["POST"])
def new_comment():
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    body = request.form["Body"]
    ## store comment
    resp = jsonify(success=True)
    return resp

@app.route("/api/comment/update", methods=["POST"])
def update_comment():
    commentId = request.form["CommentId"]
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    body = request.form["Body"]
    ## update comment
    resp = jsonify(success=True)
    return resp


@app.route("/api/comment/delete", methods=["POST"])
def delete_comment():
    commentId = request.form["CommentId"]
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    ## delete comment
    resp = jsonify(success=True)
    return resp
