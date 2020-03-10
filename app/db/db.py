import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from app.db.comment import Comment


def get_db():
    # if 'db' not in g:
    #     g.db = sqlite3.connect(
    #         current_app.config['DATABASE'],
    #         detect_types=sqlite3.PARSE_DECLTYPES
    #     )
    #     g.db.row_factory = sqlite3.Row

    from flaskext.mysql import MySQL
    if 'db' not in g:
        mysql = MySQL()
        mysql.init_app(current_app)
        g.db = mysql.connect()


    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    with current_app.open_resource('db/schema.sql') as f:
        script = f.read().decode()
        execute_script(script)
       
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.' + current_app.config['MYSQL_DATABASE_DB'])

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def execute_script(sql):
    db = get_db()
    cursor = db.cursor()
    commands = sql.split(";")
    for c in commands:
        if len(c) > 1:
            cursor.execute(c+";")

def storeEvent(event):
    connection = get_db()
    cursor = connection.cursor()
    sql_insert_query = """ INSERT INTO EventStore
                       (event, comment_id, post_id, user_id, created, body, parent_id) VALUES (%s,%s,%s,%s, %s, %s, %s);"""
    cursor.execute(sql_insert_query, (event.type, event.comment.id, event.comment.postId, event.comment.userId ,event.comment.created, event.comment.body, event.comment.parent_id))



def getComment(id):
    connection = get_db()
    cursor = connection.cursor()
    sql = """SELECT * FROM Comments WHERE id=%s;"""

    cursor.execute(sql,(id))
    result = cursor.fetchone()
    if(result == None):
        return None
    else:
        print(result)
        (id,user_id, post_id,created,body ,parent_id) = result
        comment = Comment(user_id, post_id, body,id,parent_id)
        comment.created = created
        return comment

def getCommentsUserId(userId):
    connection = get_db()
    cursor = connection.cursor()
    sql = """SELECT * FROM Comments WHERE user_id=%s;"""

    cursor.execute(sql,(userId))
    result = cursor.fetchall()
    comments = []
    if result == None:
        return comments
    for row in result:  
        print(result)
        (id,user_id, post_id,created,body ,parent_id) = row
        comment = Comment(user_id, post_id, body,id,parent_id)
        comment.created = created
        comments.append(comment)

    return comments

def getCommentsPostId(postId):
    connection = get_db()
    cursor = connection.cursor()
    sql = """SELECT * FROM Comments WHERE post_id=%s;"""

    cursor.execute(sql,(postId))
    result = cursor.fetchall()
    comments = []
    if result == None:
        return comments
    for row in result:  
        print(result)
        (id,user_id, post_id,created,body ,parent_id) = row
        comment = Comment(user_id, post_id, body,id,parent_id)
        comment.created = created
        comments.append(comment)

    return comments

def insertComment(comment):
    connection = get_db()
    cursor = connection.cursor()
    if comment.id == None:
        print("Comment.id is empty")
        sql_insert_query = """ INSERT INTO Comments
                       (post_id, user_id, created, body, parent_id) VALUES (%s,%s,%s,%s,%s);"""
        cursor.execute(sql_insert_query, ( comment.postId,
     comment.userId , comment.created, comment.body, comment.parent_id))
    else:
        print("Comment.id is " + str(comment.id))
        sql_insert_query = """ INSERT INTO Comments
                       (id, post_id, user_id, created, body, parent_id) VALUES (%s,%s,%s,%s,%s, %s);"""
        cursor.execute(sql_insert_query, ( comment.id, comment.postId,
     comment.userId , comment.created, comment.body, comment.parent_id))

    connection.commit()

def updateComment(comment):
    connection = get_db()
    cursor = connection.cursor()
    
    sql_insert_query = """ UPDATE Comments
                        SET post_id = %s,
                            user_id = %s,
                            created = %s,
                            body = %s,
                            parent_id = %s
                       WHERE id=%s ;"""
    cursor.execute(sql_insert_query, (comment.postId,
    comment.userId , comment.created, comment.body, comment.parent_id, comment.id))
    connection.commit()

def deleteComment(comment):
    
    connection = get_db()
    cursor = connection.cursor()
    
    sql_insert_query = """ DELETE Comments
                    WHERE id=%s AND user_id=%s AND post_id=%s;"""
    cursor.execute(sql_insert_query, (comment.id, comment.postId,comment.userId ))
    connection.commit()