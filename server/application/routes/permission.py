# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.permission import Permission
import json

@app.route('/permissions', methods=['GET'])
def permission_list ():
  # try:

    permissions = Permission.list_records(**request.args)

    return jsonify([p.to_dict(rules = ('-status',)) for p in permissions])
  # except:
  #   return 'query failed', 404

@app.route('/permission', methods=['GET'])
def permission_query ():

  try: 
    record = Permission().query_record(**request.args) 

    return jsonify(record.to_dict(rules = ('-status',)))

  except:
    return 'query failed', 404

@app.route('/permission', methods=['POST'])
def permission_create ():
  
  try:
    schema = json.loads(request.data)
    record = Permission.create_record(**schema)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/permission/<id>', methods=['PATCH'])
def permission_modify (id):
  try:

    schema = json.loads(request.data)
    record = Permission.modify_record(id, schema)
    return jsonify(record.to_dict())
  except:
    return 'modify failed', 400


@app.route('/permission/<id>', methods=['DELETE'])
def permission_delete (id):
  try: 
    Permission.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
  

