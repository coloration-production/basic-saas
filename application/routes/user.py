# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.user import User
import json

@app.route('/users', methods=['GET'])
def list ():
  try:
    record_dicts = []

    for i, record in enumerate(User.list_records()):
      record_dicts.append(record.to_dict())

    return jsonify(record_dicts)
  except:
    return 'query failed', 404

@app.route('/user/<id>', methods=['GET'])
def query (id):

  try: 
    record = User().query_record(id) 

    return jsonify(record.to_dict())

  except:
    return 'query failed', 404

@app.route('/user/<name>', methods=['POST'])
def create (name):
  
  try:
    user = User()
    user.name = name
    record = user.create_record(name)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/user/<id>', methods=['PATCH'])
def modify (id):
  try:
    record = User.modify_record(id, json.loads(request.data))
    return jsonify(record.to_dict())
  except:
    return 'delete failed', 400


@app.route('/user/<id>', methods=['DELETE'])
def del (id):
  try: 
    User.delete_record(id = id)
    return ''
  except:
    return 'deleted', 404
  

