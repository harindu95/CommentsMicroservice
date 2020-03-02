from app.db import db

def getComment(id):
    return db.getComment(id)

def getCommentsUserId(userId):
    return db.getCommentsUserId(userId)

def getCommentsPostId(postId):
    return db.getCommentsPostId(postId)