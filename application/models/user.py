# encoding: utf-8

import datetime
from application import db

class User (db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(16))
  created = db.Column(db.DateTime, default = datetime.datetime.now)

  def __repr__(self):
    return '<User {}:{}>'.format(self.id, self.name)

  @classmethod
  def create_record (User, name):
    record = User(name = name)
    db.session.add(record)
    db.session.commit()
    return record

  @classmethod
  def query_record (User, id):
    return User.query.filter_by(id = id).first()

  @classmethod
  def list_records (User):
    return User.query.all()

  @classmethod
  def delete_record (User, id):
    record = User.query_record(id)
    db.session.delete(record)
    db.session.commit()

  @classmethod
  def modify_record (User, id, user):
    record = User.query_record(id)
    record.name = user['name']
    db.session.add(record)
    db.session.commit()
    
    return record

  def to_dict (self):
    return {
      'id': self.id,
      'name': self.name,
      'created': self.created
    }