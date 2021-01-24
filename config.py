# encoding: utf-8

from os import path


basedir = path.abspath(path.dirname(__file__))


class Config (object):
  
  APP_NAME = 'Python Flask Boilerplate'
  DEV = False
  DEBUG = False
  HOST = '0.0.0.0'
  PORT = 5678

  SQLALCHEMY_DATABASE_URI = ''
  SQLALCHEMY_TRACK_MODIFICATIONS = False

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