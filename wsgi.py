#!/usr/bin/python3
'''WSGI application launch '''

import sys
sys.path.insert(0, '/var/www/html/CommentsMicroservice')

from app.microservice import app as application