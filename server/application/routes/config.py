from application import app
from flask_jwt import jwt_required
from application.models.user import User
from application.models.role import Role

@app.route('/config', methods = ['GET'])
@jwt_required()
def get_config ():
  config_dict = {
    'status': {
      'default': {
        '0': 'delete',
        '1': 'enable',
        '2': 'disable',
      }
    }
  }

  return config_dict, 200


@app.route('/set_default', methods = ['POST'])
def set_default ():

  record = User().query_record(id = 1) 

  if record: return { 'code': 400, 'message': 'db has initialized' }, 400

  default_role = {
    'name': 'admin',
    'alias': '管理员',
    'status': 1,
  }

  role = Role.create_record(**default_role)

  default_user = {
    'name': 'David',
    'pwd': '123456',
    'status': 1,
    'role_id': 1
  }

  user = User.create_record(**default_user)

  return {
    'user': user.to_dict(rules = ('-pwd', '-role')),
    'role': role.to_dict(rules = ('-users', )),
  }, 201