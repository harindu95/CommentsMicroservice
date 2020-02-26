from flask import Flask,jsonify
import os
from db import db
from init import create_app



app = create_app();
db.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

# Need to setup mysql beforehand
@app.route("/database")
def db_test():
    d = db.get_db()
    return "Database connected"

@app.route("/api/comment/<id>/")
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
    response['id'] = '1232'
    response['UserId'] = '23424'
    response['PostId'] = postId
    response['Body'] = 'Comment description'
    return jsonify(response)



if __name__ == "__main__":
    app.run()