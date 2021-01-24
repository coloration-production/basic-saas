# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.user import User
import json

@app.route('/users', methods=['GET'])
def list_users ():
  try:
    record_dicts = []

    for i, record in enumerate(User.list_records()):
      record_dicts.append(record.to_dict())

    return jsonify(record_dicts)
  except:
    return 'query failed', 404

@app.route('/user/<uid>', methods=['GET'])
def query_user (uid):

  try: 
    record = User().query_record(uid) 

    return jsonify(record.to_dict())

  except:
    return 'query failed', 404

@app.route('/user/<uname>', methods=['POST'])
def create_user (uname):
  
  try:
    user = User()
    user.name = uname
    record = user.create_record(uname)

    return jsonify(record.to_dict()), 201

  except:
    return 'create failed', 400

@app.route('/user/<uid>', methods=['PATCH'])
def modify_user(uid):
  try:
    record = User.modify_record(uid, json.loads(request.data))
    return jsonify(record.to_dict())
  except:
    return 'delete failed', 400


@app.route('/user/<uid>', methods=['DELETE'])
def del_user (uid):
  try: 
    User.delete_record(uid)
    return ''
  except:
    return 'deleted', 404
  

