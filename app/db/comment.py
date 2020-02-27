from datetime import datetime

class Comment:

    def __init__(self):
        self.id = 0
        self.created = datetime.now()
        self.userId = 0
        self.postId = 0
        self.body = ""
