# encoding: utf-8

from flask import jsonify, request
from application import app
from application.models.widget import Widget
from application.routes.mediaProxy import media_proxy_request
import re
import json

def format_response_dict (record, rules = ('-windows.widgets',)):

  recordCount = record.count()

  if recordCount <= 0: return record

  records = record if recordCount > 1 else [record]
  dicts = [r.to_dict(rules = rules) for r in records]
  cameras = list(filter(lambda d: d['type'] == 2, dicts))

  # 从代理列表中查找 originUrl 与 url 一致的 mediaProxy, 没有则创建一个 mediaProxy
  if len(cameras) > 0:
    mediaProxyAppName = 'camera'
    mediaResponse = media_proxy_request('getMediaList')
    mediaList = mediaResponse['data']

    for cmr in cameras:
      hasProxy = False
      for mediaProxy in mediaList:
        if mediaProxy['originUrl'] == cmr['url']:
          hasProxy = True
          cmr.update({ "info": { "src": '/{}/{}.flv'.format(mediaProxyAppName, mediaProxy['stream']) } })

      if not hasProxy:
        defaultHost = '__defaultVhost__'
        params = {
          'url': cmr['url'],
          'vhost': defaultHost,
          'stream': cmr['id'],
          'app': mediaProxyAppName,
        }

        response = media_proxy_request('addStreamProxy', **params)
        
        if response['code'] == 0:
          key = response['data']['key']
          cmr.update({ 'info': { 'src': re.sub(defaultHost, '', key) + '.flv' }})
        pass

  return jsonify(dicts) if recordCount > 1 else dicts[0]

@app.route('/widgets', methods=['GET'])
def widget_list ():
  # try:

    widgets = Widget.list_records(**request.args)
    print(-1)
    return format_response_dict(widgets)
  # except:
  #   return 'query failed', 404

@app.route('/widget', methods=['GET'])
def widget_query ():

  # try: 
    record = Widget().query_record(**request.args) 

    return format_response_dict(record)

  # except:
  #   return 'query failed', 404

@app.route('/widget', methods=['POST'])
def widget_create ():
  
  # try:
    schema = json.loads(request.data)
    record = Widget.create_record(**schema)

    return format_response_dict(record), 201

  # except:
  #   return 'create failed', 400

@app.route('/widget/<id>', methods=['PATCH'])
def widget_modify (id):
  try:

    schema = json.loads(request.data)
    record = Widget.modify_record(id, schema)
    return format_response_dict(record)
  except:
    return 'modify failed', 400


@app.route('/widget/<id>', methods=['DELETE'])
def widget_delete (id):
  try: 
    Widget.delete_record(id = id)
    return ''
  except:
    return 'delete failed', 404
