# encoding: utf-8

from app import app

@app.route('/user/<uid>', methods=['GET'])
def query_user (uid):
  return uid + ''