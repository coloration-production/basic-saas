# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.window import Window
import json

@app.route('/windows', methods=['GET'])
def window_list ():
  # try:

    windows = Window.list_records(**request.args)

    return jsonify([p.to_dict(rules = ('-widgets.windows',)) for p in windows])
  # except:
  #   return 'query failed', 404

@app.route('/window', methods=['GET'])
def window_query ():

  try: 
    record = Window().query_record(**request.args) 

    return jsonify(record.to_dict(rules = ('-widgets.windows',)))

  except:
    return 'query failed', 404

@app.route('/window', methods=['POST'])
def window_create ():
  
  # try:
    print('a')
    schema = json.loads(request.data)
    print('b')
    record = Window.create_record(**schema)
    print('c')
    return jsonify(record.to_dict(rules = ('-widgets.windows',))), 201

  # except:
  #   return 'create failed', 400

@app.route('/window/<id>', methods=['PATCH'])
def window_modify (id):
  try:

    schema = json.loads(request.data)
    record = Window.modify_record(id, schema)
    return jsonify(record.to_dict(rules = ('-widgets.windows',)))
  except:
    return 'modify failed', 400


@app.route('/window/<id>', methods=['DELETE'])
def window_delete (id):
  try: 
    Window.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
  

