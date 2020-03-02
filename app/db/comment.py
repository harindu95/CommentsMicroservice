from datetime import datetime

class Comment:

    def __init__(self ,userId, postId, body, id= None):
        self.id = id
        self.created = datetime.now()
        self.userId = userId
        self.postId = postId
        self.body = body

    # def toJson():
