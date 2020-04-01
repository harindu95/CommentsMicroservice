'''Test event handling'''

import pytest 
from unittest import mock
from flask import current_app, g, jsonify
from app import microservice, event_handler
from app.db.comment import Comment
from app.db import db
from app import query
from app.event_handler import handle_event

@pytest.fixture(scope='session')
def app():
    app = microservice.app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    testing_client = app.test_client()
    yield testing_client

@pytest.fixture 
def app_context(app):
    with app.app_context():
        yield app


@pytest.fixture
def database(app_context):
    db.init_db()
    comment = Comment(1223, 12343, "Comment body", id=1223)
    db.insertComment(comment)
    yield db

def test_event_handler(app, client, database):
    event_handler.event_buffer = []
    form = dict(UserId='3',PostId='3234',Body='comment description' ,ParentId='')
    response = client.post('/api/comment/new', data=form)     
    handle_event(0)
    comments = Comment.query.filter_by(user_id=3).all()
    assert len(comments) == 1

def test_event_handler_repeated(app, client, database):
    event_handler.event_buffer = []
    form = dict(UserId='3',PostId='3234',Body='comment description' ,ParentId='')
    response = client.post('/api/comment/new', data=form)     
    handle_event(0)
    handle_event(0)
    comments = Comment.query.filter_by(user_id=3).all()
    assert len(comments) == 2
