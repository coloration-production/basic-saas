# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
from sqlalchemy_serializer import SerializerMixin
from application.models.window_widget import registrations
from application.models.widget import Widget
from datetime import datetime

class Window(BaseEntity, SerializerMixin):

  __tablename__ = 'windows'
  
  name = db.Column(db.String(32))
  layout = db.Column(db.String)
  widgets = db.relationship(
    'Widget', 
    secondary = registrations, 
    backref = db.backref('windows', lazy = 'dynamic'), 
    lazy = 'dynamic'
  )

  def __repr__(self) -> str:
    return '<Window {}:{}>'.format(self.id, self.name)

  @classmethod
  def create_record (Entity, **kwargs):
    widgets = []
    if 'widgets' in kwargs:
      widgets = kwargs['widgets']
      del kwargs['widgets']
    record = Entity(**kwargs)
    if len(widgets) > 0 and isinstance(widgets, list):
      record.widgets = Widget.query.filter(Widget.id.in_(widgets)).all()
      pass
    db.session.add(record)
    db.session.commit()
    return record

  @classmethod
  def modify_record (Entity, id, entity):
    record = Entity.query_record(id = id)
    widgets = []

    if 'id' in entity: 
      del entity['id']
    
    if 'widgets' in entity:
      widgets = entity['widgets']
      del entity['widgets']
    
    for key in entity:
      setattr(record, key, entity[key])

    if len(widgets) > 0 and isinstance(widgets, list):
      record.widgets = Widget.query.filter(Widget.id.in_(widgets)).all()
      pass
    
    setattr(record, 'lasted', datetime.utcnow())

    db.session.add(record)
    db.session.commit()
    
    return record