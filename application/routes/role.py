# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.role import Role
import json

@app.route('/roles', methods=['GET'])
def list ():
  try:
    record_dicts = []

    for i, record in enumerate(Role.list_records()):
      record_dicts.append(record.to_dict())

    return jsonify(record_dicts)
  except:
    return 'query failed', 404

@app.route('/role/<id>', methods=['GET'])
def query (id):

  try: 
    record = Role().query_record(id) 

    return jsonify(record.to_dict())

  except:
    return 'query failed', 404

@app.route('/role/<name>', methods=['POST'])
def create (name):
  
  try:
    role = Role()
    role.name = name
    record = role.create_record(name)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/role/<id>', methods=['PATCH'])
def modify (id):
  try:
    record = Role.modify_record(id, json.loads(request.data))
    return jsonify(record.to_dict())
  except:
    return 'delete failed', 400


@app.route('/role/<id>', methods=['DELETE'])
def del (id):
  try: 
    Role.delete_record(id)
    return ''
  except:
    return 'deleted', 404
  

