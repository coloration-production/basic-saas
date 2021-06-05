# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.role import Role
import json

@app.route('/roles', methods=['GET'])
def role_list ():
  try:
    res = [r.to_dict(rules=('-users',)) for r in Role.list_records(**request.args)]
    return jsonify(res)
  except:
    return 'query failed', 404

@app.route('/role', methods=['GET'])
def role_query ():

  try: 
    record = Role().query_record(**request.args) 
    return record.to_dict(rules=('-users.role',))

  except:
    return 'query failed', 404

@app.route('/role', methods=['POST'])
def role_create ():
  
  try:
    schema = json.loads(request.data)
    record = Role.create_record(**schema)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/role/<id>', methods=['PATCH'])
def role_modify (id):
  try:

    schema = json.loads(request.data)
    record = Role.modify_record(id, schema)
    return jsonify(record.to_dict(rules = ('-users',)))
  except:
    return 'modify failed', 400


@app.route('/role/<id>', methods=['DELETE'])
def role_delete (id):
  try: 
    Role.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
  

