# encoding: utf-8

# from gevent.pywsgi import WSGIServer
from application import app
from config import Config

host = '0.0.0.0'
port = 5678

if __name__ == '__main__':

  # Development
  app.run(debug=True, host = Config.HOST, port = Config.PORT)

  # Production
  # http_server = WSGIServer((Config.HOST, Config.PORT), app)
  # http_server.serve_forever()
