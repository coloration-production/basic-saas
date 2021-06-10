# encoding: utf-8

# from gevent.pywsgi import WSGIServer
from application import app
from config import current

host = '0.0.0.0'
port = 5678

if __name__ == '__main__':

  if current.DEV:
    # Development
    app.run(debug=True, host = current.HOST, port = current.PORT)

  else:
  # Production
    http_server = WSGIServer((current.HOST, current.PORT), app)
    http_server.serve_forever()
