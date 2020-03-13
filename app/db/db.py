import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options = {
    'expire_on_commit': False
})

def get_db():
    return db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
  
    db.drop_all()
    # db.session.commit()
    db.create_all()
       
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.' + current_app.config['MYSQL_DATABASE_DB'])

def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def insertComment(comment):
    db.session.add(comment)
    db.session.commit()


def updateComment(comment):
    c = Comment.query.filter_by(id = comment.id).first()
    if c != None:
        c.update(comment.serialize())
        db.session.commit()

def deleteComment(comment):
    c = Comment.query.filter_by(id = comment.id).first()
    if c != None:
        c.delete()
        db.session.commit()

