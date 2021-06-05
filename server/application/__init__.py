# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import logging

app = Flask(__name__)

app.config.from_object('config.current')

db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

'''

'''

import application.jwt

import application.routes.user
import application.routes.permission
import application.routes.role
import application.routes.access




# after Model defined
db.create_all()