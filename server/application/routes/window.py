# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.window import Window
from application.routes.widget import format_response_dict
import json

def _format_response_dict (record, rules = ('-widgets.windows',)):
  dictionary = record.to_dict(rules = rules)


  widgets = [format_response_dict(wdg, rules = ('-windows',), single = True) for wdg in record.widgets]
  dictionary['widgets'] = widgets

  return dictionary

@app.route('/windows', methods=['GET'])
def window_list ():
  # try:

    windows = Window.list_records(**request.args)

    return jsonify([_format_response_dict(p) for p in windows])
  # except:
  #   return 'query failed', 404

@app.route('/window', methods=['GET'])
def window_query ():

  # try: 
    record = Window().query_record(**request.args) 
    return _format_response_dict(record)

  # except:
  #   return 'query failed', 404

@app.route('/window', methods=['POST'])
def window_create ():
  
  # try:
    schema = json.loads(request.data)
    record = Window.create_record(**schema)
    return _format_response_dict(record), 201

  # except:
  #   return 'create failed', 400

@app.route('/window/<id>', methods=['PATCH'])
def window_modify (id):
  # try:

    schema = json.loads(request.data)
    record = Window.modify_record(id, schema)
    return _format_response_dict(record)
  # except:
  #   return 'modify failed', 400


@app.route('/window/<id>', methods=['DELETE'])
def window_delete (id):
  try: 
    Window.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
  

