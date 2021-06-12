from flask import request
from application import app
from application.logic.mediaProxy import media_proxy_request

excludeMethods = (
  'getServerConfig',
  'setServerConfig',
  'restartServer'
)

@app.route('/media/<method>', methods = ['GET'])
def media_server(method):
  return media_proxy_request(method, **request.args)