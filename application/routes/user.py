# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.user import User
import json

@app.route('/users', methods=['GET'])
def user_list ():
  try:
    # record_dicts = []

    # for i, record in enumerate(User.list_records(**request.args)):
    #   record_dicts.append(record.to_dict())

    users = User.list_records(**request.args)
    return jsonify([u.to_dict(rules=('-role.users',)) for u in users])
  except:
    return 'query failed', 404

@app.route('/user', methods=['GET'])
def user_query ():

  try: 
    record = User().query_record(**request.args) 

    return jsonify(record.to_dict(
      rules=('-pwd', '-role.users')
    ))

  except:
    return 'query failed', 404

@app.route('/user', methods=['POST'])
def user_create ():
  
  try:
    schema = json.loads(request.data)
    record = User.create_record(**schema)

    return jsonify(record.to_dict(rules=('-pwd', '-role.users'))), 201

  except:
    return 'create failed', 400

@app.route('/user/<id>', methods=['PATCH'])
def user_modify (id):
  try:
    schema = json.loads(request.data)

    if 'pwd' in schema: del schema['pwd']

    record = User.modify_record(id, schema)
    return jsonify(record.to_dict('-pwd', '-role.users'))
  except:
    return 'modify failed', 400


@app.route('/user/<id>', methods=['DELETE'])
def user_delete (id):
  try: 
    User.delete_record(id = id)
    return ''
  except:
    return 'deleted', 404


