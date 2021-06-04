# encoding: utf-8

import datetime
from application import db

class User (db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(16))
  pwd = db.Column(db.String(32))
  status = db.Column(db.Integer, default = 1)
  created = db.Column(db.DateTime, default = datetime.datetime.now)
  role = db.relationship('Role', backref = 'user')
  
  def __repr__(self):
    return '<User {}:{}>'.format(self.id, self.name)

  @classmethod
  def create_record (User, **kwargs):
    
    record = User(**kwargs)
    db.session.add(record)
    db.session.commit()

    return record

  @classmethod
  def query_record (User, **kwargs):
    return User.query.filter_by(**kwargs).first()

  @classmethod
  def list_records (User):
    return User.query.all()

  @classmethod
  def delete_record (User, **kwargs):
    record = User.query_record(**kwargs)
    db.session.delete(record)
    db.session.commit()

  @classmethod
  def modify_record (User, id, user):
    record = User.query_record(id)
    
    if 'id' in user: 
      del user['id']
    
    record.update(user)
    db.session.add(record)
    db.session.commit()
    
    return record

  def to_dict (self):
    return {
      'id': self.id,
      'name': self.name,
      'created': self.created
    }