# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.permission import Permission
import json

@app.route('/permissions', methods=['GET'])
def list ():
  try:
    record_dicts = []

    for i, record in enumerate(Permission.list_records()):
      record_dicts.append(record.to_dict())

    return jsonify(record_dicts)
  except:
    return 'query failed', 404

@app.route('/permission/<id>', methods=['GET'])
def query (id):

  try: 
    record = Permission().query_record(id) 

    return jsonify(record.to_dict())

  except:
    return 'query failed', 404

@app.route('/permission/<uname>', methods=['POST'])
def create (uname):
  
  try:
    per = Permission()
    per.name = uname
    record = per.create_record(uname)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/permission/<id>', methods=['PATCH'])
def modify (id):
  try:
    record = Permission.modify_record(id, json.loads(request.data))
    return jsonify(record.to_dict())
  except:
    return 'delete failed', 400


@app.route('/permission/<id>', methods=['DELETE'])
def del (id):
  try: 
    Permission.delete_record(id)
    return ''
  except:
    return 'deleted', 404
  

