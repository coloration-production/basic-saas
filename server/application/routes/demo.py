# encoding: utf-8

from flask import request, jsonify
import json
from application import app

@app.route('/demo/param/<name>', methods=['GET'])
def demo_param (name):
  return '<h1>Hello, {}!<h1>'.format(name)


@app.route('/demo/query', methods=['GET'])
def demo_query ():
  # Query String: ?grade=2&class=6
  try:
    # default None
    grade_num = request.args.get('grade', None)
    # Error Go except
    class_num = request.args['class']

    return jsonify({ 'Class': class_num, 'Grade': grade_num })

  except:

    return jsonify({ 'message': '参数错误' }), 400


@app.route('/demo/json', methods=['POST'])
def demo_json ():
  # str => dict
  # 数组第一项的url
  try:
    url = json.loads(request.data)[0]['url']
    
    return jsonify({ 'url': url })
  
  except:
    
    return jsonify({ 'message': '数组为空' }), 400 

@app.route('/demo/form', methods=['POST'])
def demo_form ():
  # FormData 从 request.form 中获取

  return jsonify(request.form)