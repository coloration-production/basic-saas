# encoding: utf-8

from gevent.pywsgi import WSGIServer
from application import app

if __name__ == '__main__':

  print('????', app.config['DEV'], type(app.config['DEV']), app.config['MEDIA_SERVICE_RESTFUL_API_URL'], type(app.config['MEDIA_SERVICE_RESTFUL_API_URL']))
  if app.config['DEV']:
    # Development
    app.run(
      debug = app.config['DEBUG'], 
      host = app.config['HOST'], 
      port = app.config['PORT'])

  else:
  # Production
    http_server = WSGIServer((app.config['HOST'], app.config['PORT']), app)
    http_server.serve_forever()
