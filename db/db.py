import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


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
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def execute_script(sql):
    db = get_db()
    cursor = db.cursor();
    commands = sql.split(";");
    for c in commands:
        if len(c) > 1:
            cursor.execute(c+";")