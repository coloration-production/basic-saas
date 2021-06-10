from application import db

registrations = db.Table(
  'registrations',
  db.Column('window_id', db.Integer, db.ForeignKey('windows.id'), primary_key = True),
  db.Column('widget_id', db.Integer, db.ForeignKey('widgets.id'), primary_key = True),
)