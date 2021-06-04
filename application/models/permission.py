# encoding: utf-8

import datatime
from application import db

class Permission (db.Model):
  __tablename__ = 'permissions'

  id = db.Column(db.Integer, primary_key = True)
  pid = db.Column(db.Integer, default = 0)
  name = db.Column(db.String(16))
  alias = db.Column(db.String(16))
  type = db.Column(db.Integer)
  created = db.Column(db.DateTime, default = datetime.datetime.now)

  def __repr__(self) -> str:
      return '<Permission {}:{}>'.format(self.id, self.name)
  
  @classmethod
  def create_record (Permission, name, type, alias = ''):
    record = Permission(name = name, type = type, alias = alias)
    db.session.add(record)
    db.session.commit()
    return record

  @classmethod
  def query_record (Permission, id):
    return Permission.query.filter_by(id = id).first()

  @classmethod
  def list_records (Permission):
    return Permission.query.all()

  @classmethod
  def delete_record (Permission, id):
    record = Permission.query_record(id)
    db.session.delete(record)
    db.session.commit()

  @classmethod
  def modify_record (Permission, id, permission):
    record = Permission.query_record(id)
    record.name = permission['name']
    record.type = permission['type']
    record.alias = permission['alias']
    db.session.add(record)
    db.session.commit()
    
    return record

  def to_dict (self):
    return {
      'id': self.id,
      'name': self.name,
      'alias': self.alias,
      'created': self.created
    }