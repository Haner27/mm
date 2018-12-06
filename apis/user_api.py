from . import *

user_app = Blueprint('user', __name__, url_prefix='/api/user')


@user_app.before_request
def before_request():
    print('before_request')


@user_app.route('/get', methods=['GET'])
def get_user():
    return error('没有找到用户')


@user_app.route('/create', methods=['POST'])
@ApiDoc.add_description('创建用户')
@ApiDoc.add_body_field('username', str, example='hannengfang', validators=[Required])
@ApiDoc.add_body_field('password', str, example='xxxxxxxxxxx', validators=[Required])
@ApiDoc.add_body_field('age', int, example=10, validators=[Required])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age', int)
    return response(data=dict(username=username, age=age))


