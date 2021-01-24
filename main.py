# encoding: utf-8

# from gevent.pywsgi import WSGIServer
from application import app

host = 'localhost'
port = 5678

if __name__ == '__main__':

  # Development
  app.run(debug=True, host = host, port = port)

  # Production
  # http_server = WSGIServer(('0.0.0.0', port), app)
  # http_server.serve_forever()
