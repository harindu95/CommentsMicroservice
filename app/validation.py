from schema import Schema, Optional, Use, Or

def stringEmpty(input):
    if not input.strip():
        return 0
    else:
        raise Exception("String not empty")

errors ={
    'CommentId':'Invalid CommentId: CommentId should be an Integer',
    'UserId':'Invalid UserId: UserId should be an Integer',
    'PostId':'Invalid PostId: PostId should be an Integer',
    'ParentId':'Invalid ParentId: ParentId should be an Integer',
}

newCommentSchema = Schema({
    'UserId' : Use(int, error=errors['UserId']),
    'PostId': Use(int, error=errors['PostId']),
    'Body' : Use(str),
    Optional('ParentId'): Or(Use(int, error=errors['ParentId']),
     Use(stringEmpty, error=errors['ParentId']))
})


updateCommentSchema = Schema({
    'CommentId' : Use(int, error=errors['CommentId']),
    'UserId' : Use(int, error=errors['UserId']),
    'PostId': Use(int, error=errors['PostId']),
    'Body' : Use(str),
    Optional('ParentId'): Or(Use(int, error=errors['ParentId']),
     Use(stringEmpty, error=errors['ParentId']))
})


deleteCommentSchema = Schema({
    'CommentId' : Use(int, error=errors['CommentId']),
    'UserId' : Use(int, error=errors['UserId']),
    'PostId': Use(int, error=errors['PostId']),
    })


def schema_message(e):
    for m in e.errors:
        if m != None:
            return m

    return None
