from application import app
from flask_jwt import current_identity, jwt_required


@app.route('/signout', methods = ['PATCH'])
@jwt_required()
def signout ():
  return 'sign out.'

@app.route('/protected')
@jwt_required()
def protected ():
  return '%s' % current_identity
