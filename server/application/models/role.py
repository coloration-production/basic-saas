# encoding: utf-8

from application.models.base_entity import BaseEntity
from application import db
from sqlalchemy_serializer import SerializerMixin

class Role (BaseEntity, SerializerMixin):

  __tablename__ = 'roles'

  name = db.Column(db.String(16))
  alias = db.Column(db.String(16))
  users = db.relationship('User', backref = 'role', lazy = 'dynamic')

  def __repr__(self) -> str:
      return '<Role {}:{}>'.format(self.id, self.name)

