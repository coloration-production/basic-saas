# encoding: utf-8

from os import path
from datetime import timedelta

basedir = path.abspath(path.dirname(__file__))


class Config (object):
  
  APP_NAME = 'Python Flask Boilerplate'
  DEV = False
  DEBUG = False
  HOST = '0.0.0.0'
  PORT = 5678
  USER_DEFAULT_PASSWORD = '123456'
  SQLALCHEMY_DATABASE_URI = ''
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  '''Flask-JWT'''
  SECRET_KEY = 'super-secret'
  JWT_AUTH_URL_RULE = '/signin'
  JWT_AUTH_USERNAME_KEY = 'name'
  JWT_AUTH_PASSWORD_KEY = 'pwd'
  JWT_EXPIRATION_DELTA = timedelta(seconds = 1800)

class DevelopmentConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'db.sqlite')
  SQLALCHEMY_MIGRATE_REPO = path.join(basedir, 'db', 'db_repository')
  DEBUG = True
  DEV = True


class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@server_ip:server_port/db_name'
  DEBUG = False
  DEV = False

class TestingConfig(DevelopmentConfig):
  DEV = False
  



current = DevelopmentConfig