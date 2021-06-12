from flask import request
import requests
import json

excludeMethods = (
  'getServerConfig',
  'setServerConfig',
  'restartServer'
)

def media_proxy_request(method, **kwargs):

  if method in excludeMethods: return

  secret = '035c73f7-bb6b-4889-a715-d9eb2d1925cc'
  params = dict(kwargs)
  params['secret'] = secret
  response = requests.post('http://localhost:8080/index/api/' + method, params = params)
  
  # return response.text
  return json.loads(response.text)