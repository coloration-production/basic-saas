# encoding: utf-8

from application import db


class BaseEntity (db.Model):

  """ don't create table in db """
  __abstract__ = True


  id = db.Column(db.Integer, primary_key = True)
  status = db.Column(db.Integer,default = 1)
  
  @classmethod
  def create_record (Entity, **kwargs):
    
    record = Entity(**kwargs)
    db.session.add(record)
    db.session.commit()

    return record

  @classmethod
  def query_record (Entity, **kwargs):
    return Entity.query.filter_by(**kwargs).first()

  @classmethod
  def list_records (Entity, **kwargs):
    return Entity.query.filter_by(**kwargs)

  @classmethod
  def delete_record (Entity, **kwargs):
    record = Entity.query_record(**kwargs)
    db.session.delete(record)
    db.session.commit()

  @classmethod
  def modify_record (Entity, id, entity):
    record = Entity.query_record(id = id)
    
    if 'id' in entity: 
      del entity['id']
    
    for key in entity:
      setattr(record, key, entity[key])
    
    db.session.add(record)
    db.session.commit()
    
    return record
