# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
from sqlalchemy_serializer import SerializerMixin
from application.logic.mediaProxy import media_proxy_request

mediaProxyAppName = 'camera'

class Widget (BaseEntity, SerializerMixin):

  __tablename__ = 'widgets'
  
  name = db.Column(db.String(32))
  url = db.Column(db.String(256))
  type = db.Column(db.Integer)
  

  def __repr__(self) -> str:
    return '<Widget {}:{}>'.format(self.id, self.name)

