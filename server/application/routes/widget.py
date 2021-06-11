# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.widget import Widget
import json

@app.route('/widgets', methods=['GET'])
def widget_list ():
  try:

    widgets = Widget.list_records(**request.args)

    return jsonify([p.to_dict(rules = ('-windows.widgets',)) for p in widgets])
  except:
    return 'query failed', 404

@app.route('/widget', methods=['GET'])
def widget_query ():

  try: 
    record = Widget().query_record(**request.args) 

    return jsonify(record.to_dict(rules = ('-windows.widgets',)))

  except:
    return 'query failed', 404

@app.route('/widget', methods=['POST'])
def widget_create ():
  
  # try:
    schema = json.loads(request.data)
    record = Widget.create_record(**schema)

    return jsonify(record.to_dict(rules = ('-windows.widgets',))), 201

  # except:
  #   return 'create failed', 400

@app.route('/widget/<id>', methods=['PATCH'])
def widget_modify (id):
  try:

    schema = json.loads(request.data)
    record = Widget.modify_record(id, schema)
    return jsonify(record.to_dict(rules = ('-windows.widgets',)))
  except:
    return 'modify failed', 400


@app.route('/widget/<id>', methods=['DELETE'])
def widget_delete (id):
  try: 
    Widget.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404

@app.route('/widget/join_camera/<id>', methods=['GET'])
def widget_join_camera (id):

  record = Widget().query_record(id = id)r
  
  pass
