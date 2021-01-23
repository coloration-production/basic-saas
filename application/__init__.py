from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



import application.routes.user

# after Model defined
db.create_all()