import pytest 
from unittest import mock
from flask import current_app, g
from app import microservice
from app.db.comment import Comment
from app.db import db



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
    comment = Comment(1223, 12343, "Comment body", id=1223)
    db.storeComment(comment)
    c = db.getComment(1223)
    yield db


def test_database_connection(client):
     response = client.get('/database')
     assert response.status_code == 200
     assert b"Database connected" in response.data

def test_add_comment(client):
    form = dict(UserId='1223',PostId='3234',Body='comment description')
    response = client.post('/api/comment/new', data=form)
    assert response.status_code == 200
   
def test_get_comment(client ,database):
    
    response = client.get('/api/comment/id/1223/')
    assert response.status_code == 200
    assert b"1223" in response.data

