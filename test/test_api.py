import pytest 
from unittest import mock
from flask import current_app, g
from CommentsMicroservice import microservice


@pytest.fixture
def client():
    app = microservice.app
    app.config['MYSQL_DATABASE_USER'] = 'microservice'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'comments'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

def test_database_connection(client):
     response = client.get('/database')
     assert response.status_code == 200
     assert b"Database connected" in response.data
    
def test_get_comment(client):
    response = client.get('/api/comment/1233/')
    assert response.status_code == 200
    assert b"1233" in response.data