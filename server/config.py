# encoding: utf-8

from os import path, getenv
from datetime import timedelta
import ast

basedir = path.abspath(path.dirname(__file__))

class Config (object):
  
  APP_NAME = getenv('APP_NAME', 'Python Flask Boilerplate') 
  DEV = ast.literal_eval(getenv('DEV', 'True'))
  DEBUG = ast.literal_eval(getenv('DEBUG', 'True'))
  HOST = '0.0.0.0'
  PORT = 5678
  USER_DEFAULT_PASSWORD = '123456'
  SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + path.join(basedir, 'db.sqlite'))
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_MIGRATE_REPO = path.join(basedir, 'db', 'db_repository')

  '''Flask-JWT'''
  SECRET_KEY = 'super-secret'
  JWT_AUTH_URL_RULE = '/signin'
  JWT_AUTH_USERNAME_KEY = 'name'
  JWT_AUTH_PASSWORD_KEY = 'pwd'
  JWT_EXPIRATION_DELTA = timedelta(seconds = 1800)

  '''Docker-Network media-service container'''
  MEDIA_SERVICE_RESTFUL_API_URL = getenv('MEDIA_SERVICE_RESTFUL_API_URL', 'http://localhost:8080/index/api')
  MEDIA_SERVICE_SECRET = '035c73f7-bb6b-4889-a715-d9eb2d1925cc'

  ### SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@server_ip:server_port/db_name'


current = Config