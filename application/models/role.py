# encoding: utf-8

import datatime
from application import db

class Role (db.Model):
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(16))
  created = db.Column(db.DateTime, default = datetime.datetime.now)
  pers = db.relationship('Permission', backref = 'role')

  def __repr__(self) -> str:
      return '<Role {}:{}>'.format(self.id, self.name)
  
  @classmethod
  def create_record (Role, name, type, alias = ''):
    record = Role(name = name, type = type, alias = alias)
    db.session.add(record)
    db.session.commit()
    return record

  @classmethod
  def query_record (Role, id):
    return Role.query.filter_by(id = id).first()

  @classmethod
  def list_records (Role):
    return Role.query.all()

  @classmethod
  def delete_record (Role, id):
    record = Role.query_record(id)
    db.session.delete(record)
    db.session.commit()

  @classmethod
  def modify_record (Role, id, role):
    record = Role.query_record(id)
    record.name = role['name']
    record.type = role['type']
    record.alias = role['alias']
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