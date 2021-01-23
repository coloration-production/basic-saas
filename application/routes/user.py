# encoding: utf-8

from flask import jsonify
from application import app
from application.models.user import User

@app.route('/users', methods=['GET'])
def list_users ():
  try:
    record_dicts = []

    for i, record in enumerate(User.list_records()):
      record_dicts.append(record.to_dict())

    return jsonify(record_dicts)
  except:
    return jsonify('查询失败'), 404

@app.route('/user/<uid>', methods=['GET'])
def query_user (uid):

  try: 
    record = User().query_record(uid) 

    return jsonify(record.to_dict())

  except:
    return jsonify('查询失败'), 404

@app.route('/user/<uname>', methods=['POST'])
def create_user (uname):
  
  try:
    user = User()
    user.name = uname
    record = user.create_record(uname)

    return jsonify(record.to_dict()), 201

  except:
    return jsonify('创建失败'), 400

@app.route('/user/<uid>', methods=['DELETE'])
def del_user (uid):
  User.delete_record(uid)
  return '', 200
  

