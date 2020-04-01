'''Schemas for validating user input'''

from schema import Schema, Optional, Use, Or
from app.logging import log

def stringEmpty(input):
    '''Return 0 if string is empty. Else raise an exception '''
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

commentIdSchema =  Schema(Use(int, error=errors['CommentId']))
userIdSchema =  Schema(Use(int, error=errors['UserId']))
postIdSchema =  Schema(Use(int, error=errors['PostId']))

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
    })


def schema_message(e):
    '''Filter empty error messages'''
    for m in e.errors:
        if m != None:
            log.error(m)
            return m

    for m in e.autos:
        if m != None:
            log.error(m)
            return m
            
    return None
