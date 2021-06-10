# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object('config.current')

db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

'''

'''

import application.jwt

import application.routes.config
import application.routes.user
import application.routes.permission
import application.routes.role
import application.routes.access




# after Model defined
db.create_all()