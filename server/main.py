# encoding: utf-8

from gevent.pywsgi import WSGIServer
from application import app

if __name__ == '__main__':

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
