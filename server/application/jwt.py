from application import app
from flask_jwt import JWT
from flask import jsonify

from application.models.user import User

jwt = JWT(app, User.authenticate, User.identity)

@jwt.auth_response_handler
def jwt_customized_response_handler(access_token, identity):
  return jsonify({
    'access_token': access_token.decode('utf-8'),
    'user': identity.to_dict(rules = ('-role.users', '-pwd'))
  })

@jwt.jwt_error_handler
def jwt_customized_error_handler(error):
  return jsonify({
    'message': error.description,
    'code': error.status_code
  }), error.status_code