import pytest 
from unittest import mock
from flask import current_app, g, jsonify
from app import microservice

from app.db import db
from app.db.comment import Comment

@pytest.fixture(scope='session')
def app():
    app = microservice.app  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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
    database = db.get_db()
    database.session.add(comment)
    database.session.commit()
    yield db


def test_database_connection(client):
     response = client.get('/database')
     assert response.status_code == 200
     assert b"Database connected" in response.data

def test_add_comment(client):
    form = dict(UserId='1223',PostId='3234',Body='comment description' ,ParentId='')
    response = client.post('/api/comment/new', data=form)
    assert response.status_code == 200
   
def test_get_comment(client ,database):
    response = client.get('/api/comment/id/1223/')
    assert response.status_code == 200
    assert b"1223" in response.data

def test_get_comment_invalid_id(client, database):
    response = client.get('/api/comment/id/1/')
    assert response.status_code == 200
    assert b"comment doesn't exist" in response.data

def test_update_comment(client, database):
    form = dict(UserId='1223',PostId='3234',Body='comment description' , CommentId='1223', ParentId='')
    response = client.post('/api/comment/update', data=form)
    assert response.status_code == 200
    # c = db.getComment(1223)
    # assert c.body == 'comment description'
    
def test_delete_comment(client, database):
    form = dict(UserId='1223',PostId='3234',Body='comment description',CommentId='1223',ParentId='')
    response = client.post('/api/comment/delete', data=form)
    assert response.status_code == 200

def test_get_comment_by_post_id(client ,database):
    response = client.get('/api/comments/postId/478')
    assert response.status_code == 200
    
def test_get_comment_by_invalid_post_id(client,database):
    response = client.get('/api/comments/postId/125')
    assert response.status_code == 200
    assert b"no comments posted under post" in response.data
   
def test_get_comment_by_user_id(client ,database):
    response = client.get('/api/comments/userId/478')
    assert response.status_code == 200
    
def test_get_comment_by_invalid_user_id(client,database):
    response = client.get('/api/comments/userId/125')
    assert response.status_code == 200
    assert b"no comments posted by user" in response.data
    

