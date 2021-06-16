import requests
import json
import aiohttp
import asyncio
from application import app
from application.util import asyncPost
import asyncio

excludeMethods = (
  'getServerConfig',
  'setServerConfig',
  'restartServer'
)

loop = asyncio.get_event_loop()

def media_proxy_request(method, **kwargs):

  if method in excludeMethods: return
  
  params = dict(kwargs)
  params['secret'] = app.config['MEDIA_SERVICE_SECRET']
  url = app.config['MEDIA_SERVICE_RESTFUL_API_URL'] + '/' + method
  response = loop.run_until_complete(asyncPost(url, params))
  return json.loads(response)
