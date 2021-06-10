# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
import datetime
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

class User (BaseEntity, SerializerMixin):

  __tablename__ = 'users'

  name = db.Column(db.String(16))
  pwd = db.Column(db.String(128))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  
  def __repr__(self):
    return '<User {}:{}>'.format(self.id, self.name)


  @property
  def password (self):
    raise AttributeError('password is not a readable attribute')
  
  @password.setter
  def password (self, password):
    self.pwd = generate_password_hash(password)
  
  def verify_password(self, password):
    return check_password_hash(self.pwd, password)

  def ping (self):
    self.lasted = datetime.datetime.utcnow()
    
    db.session.add(self)
    db.session.commit()

  @classmethod
  def create_record (User, **kwargs):

    password = Config.USER_DEFAULT_PASSWORD if 'pwd' not in kwargs else kwargs['pwd']

    record = User(**kwargs)
    record.password = password
    db.session.add(record)
    db.session.commit()

    return record

  @classmethod
  def authenticate (User, name, pwd):
    user = User.query_record(name = name)
    if user and user.verify_password(pwd):
      return user

  @classmethod
  def identity (User, payload):
    id = payload['identity']
    user = User.query_record(id = id)

    return user, 201