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
    if comment is None :
        return jsonify({"status":"error", "message":"comment doesn't exist"}, 400)
    else:
        return comment.toJson()


@app.route("/api/comments/userId/<userId>")
def comments_by_user_id(userId):
    comments = query.getCommentsUserId(userId)
    response = []
    if not comments :
        return jsonify({"status":"error", "message":"no comments posted by user"}, 400)
    else:
        for comment in comments:
            response.append(comment.toJson())
        return jsonify(response)


@app.route("/api/comments/postId/<postId>")
def comments_by_post_id(postId):
    comments = query.getCommentsPostId(postId)
    response = []
    if not comments :
        return jsonify({"status":"error", "message":"no comments posted under post"}, 400)
    else:
        for comment in comments:
            response.append(comment.toJson())
        return jsonify(response)

    

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

# def validate_commentId(self, commentId):
#         if ceil(commentId) != commentId
#             raise ValidationError('Comment Id must be numerical only.')
# def validate_bodyLength(self, body):
#     length = SELECT LEN(body);
#         if length > 140
#             raise ValidationError('Comment is too long.')


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
    userId = request.form["UserId"]
    postId = request.form["PostId"]
    commentId = request.form["CommentId"]
    command.delete_comment(commentId, userId, postId)
    resp = jsonify(success=True)
    return resp

# def validate_postId(self, postId):
#         if ceil(postId) != postId
#             raise ValidationError('Post Id must be numerical only.')
# def validate_commentId(self, commentId):
#         if ceil(commentId) != commentId
#             raise ValidationError('Comment Id must be numerical only.')
