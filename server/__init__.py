# coding=utf-8

from flask import Flask, request, jsonify, abort
from passlib.apps import custom_app_context as pwd_context

# 配置数据库信息
from flask_sqlalchemy import SQLAlchemy

from flask_jwt import JWT, jwt_required, current_identity,timedelta

# token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)

# 连接数据库
dbhost = 'localhost:3306'
dbuser = 'root'
dbpass = 'wy939166'
dbname = 'login'
DB_URI = 'mysql+pymysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname
#
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=6000)

# 数据库
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(200))

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# jwt 鉴权

def authenticate(username, password):
    print("JWT jianquanzhong...", username, password)
    user = User.query.filter_by(username=username).first()
    if user is not None and user.verify_password(password):
        return user
    else:
        abort(401)

# jwt 身份识别

def identity(payload):
    print("JWT payload", payload)
    # 类似 ('JWT payload', {u'iat': 1489495003, u'exp': 1489501003, u'nbf': 1489495003, u'identity': 36})
    user_id = payload['identity']
    user = User.query.filter_by(id=user_id).first()
    print user
    # 返回当前身份
    return user.username

jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


@app.before_first_request
def first_request():
    db.create_all()


@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, Authorization, Content-Type, Accept, Key')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, PUT, POST, DELETE')
    return response

@app.errorhandler(401)
def custom_401(error):
    return "Something happend"

@app.route('/reg', methods=['POST'])
def reg_user():
    username = request.get_json()['username']
    password = request.get_json()['password']
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({"msg":"该用户名已经被使用，请换个用户名注册","errcode":1})
    if not username or not password:
        return jsonify({"msg": "用户名或者密码未填写，请重新填写","errcode":2})
    data = User(username=username)
    data.hash_password(password)
    db.session.add(data)
    db.session.commit()
    return jsonify({"username": data.username})



@app.route('/hello', methods=['GET'])
@jwt_required()
def hello():
    return '%s' % current_identity



if __name__ == '__main__':
    app.run(debug=True)
