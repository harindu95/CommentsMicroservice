import pytest 
from unittest import mock
from flask import current_app, g, jsonify
from app import microservice, event_handler
from app.db.comment import Comment
from app.db import db
from app import query

@pytest.fixture(scope='session')
def app():
    app = microservice.app
    app.config['MYSQL_DATABASE_USER'] = 'microservice'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'test_comments'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
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
    c = db.getComment(1223)
    yield db

def test_event_buffer(client, database):
    event_handler.event_buffer = []
    form = dict(UserId='1223',PostId='3234',Body='comment description' ,ParentId='')
    response = client.post('/api/comment/new', data=form)
    assert response.status_code == 200
    assert len(event_handler.event_buffer) == 1

def test_event_handler(client, database):
    event_handler.event_buffer = []
    form = dict(UserId='3',PostId='3234',Body='comment description' ,ParentId='')
    response = client.post('/api/comment/new', data=form)
    assert len(event_handler.event_buffer) == 1
    event_handler.handle_event()
    assert len(event_handler.event_buffer) == 0
    comments = db.getCommentsUserId(3)
    assert len(comments) == 1
