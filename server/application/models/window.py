# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
from sqlalchemy_serializer import SerializerMixin
from application.models.window_widget import registrations
from application.models.widget import Widget

class Window(BaseEntity, SerializerMixin):

  __tablename__ = 'windows'
  
  name = db.Column(db.String(32))
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
    print(0)  
    widgets = []
    
    if 'widgets' in kwargs:
      widgets = kwargs['widgets']
      del kwargs['widgets']

    print(1, widgets)    
    record = Entity(**kwargs)
    
    print(2)
    if len(widgets) > 0 and isinstance(widgets, list):
      print(3)
      record.widgets = Widget.query.filter(Widget.id.in_(widgets)).all()
      print(4)
      pass
    
    print(5)
    db.session.add(record)
    db.session.commit()

    return record