# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.role import Role
from flask_jwt import jwt_required
import json

def format_request_params (params_json):
  params = json.loads(params_json)
  
  if 'permissions' in params:
    if isinstance(params['permissions'], list):
      try:
        params['permissions'] = ','.join([str(p) for p in params['permissions']])
      except:
        del params['permissions']
    else:
      del params['permissions']
  
  return params 

def formart_response_dict (record, rules = ('-users', )):
  d = record.to_dict(rules = rules)

  print(d['permissions'])
  if len(d['permissions']) == 0:
    d['permissions'] = []
  else:
    d['permissions'] = [int(p) for p in d['permissions'].split(',')]
  pass

  return d

@app.route('/roles', methods=['GET'])
@jwt_required()
def role_list ():
  # try:
    res = [formart_response_dict(r) for r in Role.list_records(**request.args)]
    return jsonify(res)
  # except:
  #   return 'query failed', 404

@app.route('/role', methods=['GET'])
@jwt_required()
def role_query ():

  try: 
    record = Role().query_record(**request.args) 
    return formart_response_dict(record)

  except:
    return 'query failed', 404

@app.route('/role', methods=['POST'])
@jwt_required()
def role_create ():
  
  try:
    params = format_request_params(request.data)
    record = Role.create_record(**params)

    return formart_response_dict(record), 201

  except:
    return 'create failed', 400

@app.route('/role/<id>', methods=['PATCH'])
@jwt_required()
def role_modify (id):
  try:
    params = format_request_params(request.data)
    record = Role.modify_record(id, params)
    return formart_response_dict(record)
  except:
    return 'modify failed', 400


@app.route('/role/<id>', methods=['DELETE'])
@jwt_required()
def role_delete (id):
  try: 
    Role.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
  

