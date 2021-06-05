# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
from sqlalchemy_serializer import SerializerMixin

class Permission (BaseEntity, SerializerMixin):

  __tablename__ = 'permissions'
  
  pid = db.Column(db.Integer, default = 0)
  name = db.Column(db.String(16))
  alias = db.Column(db.String(16))

  def __repr__(self) -> str:
    return '<Permission {}:{}>'.format(self.id, self.name)

