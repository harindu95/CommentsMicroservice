'''This module handles database interactions'''

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options = {
    'expire_on_commit': False
})


def get_db():
    '''Return database connection'''
    return db


def init_db():
    '''Initialize database. Drop the tables and recreate them.'''
    db.drop_all()
    # db.session.commit()
    db.create_all()
       
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    db.init_app(app)



def insertComment(comment):
    '''Insert comment into database
    
    Args:
        comment (Comment) : Comment to be stored in database 
    '''
    db.session.add(comment)
    db.session.commit()


def updateComment(comment):
    '''Update existing comment from database.
    
    Args:
        comment (Comment) : Comment to be stored in database 
    '''
    from app.db.comment import Comment
    c = Comment.query.filter_by(id = comment.id).first()

    if c != None:
        c.update(comment)
        db.session.commit()

def deleteComment(comment):
    '''Delete existing comment from database.
    
    Args:
        comment (Comment) : Comment to be deleted in database 
    '''
    from app.db.comment import Comment
    c = Comment.query.filter_by(id = comment.id).first()
    if c != None:
        db.session.delete(c)
        db.session.commit()

