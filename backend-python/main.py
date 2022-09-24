from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root:halflife2@127.0.0.1/test'

db = SQLAlchemy(app)

#Database Models
class UserModel(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    
    #Similar To String Literal in JS
    def __repr__(self):
        return f"User(id={id}, username={self.username})"

class AccountType(db.Model):
    __tablename__ = 'account_type'
    
    id = db.Column(db.Integer, primary_key=True)
    typename = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"AccountType(id={self.id},typename={self.typename})"

class Account(db.Model):
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    acct_type = db.Column(db.Integer, db.ForeignKey('account_type.id'), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    #Relations
    users = db.relationship('UserModel', backref='account', lazy=True)
    account_type = db.relationship('AccountType', backref='account', lazy=True)

    def __repr__(self):
        return f"Account(id={id},user_id={self.user_id},acct_type={self.acct_type},balance={self.balance})"



#@marshal_with => Takes results value from database and take into the JSON field, serialize it ino a JSON format

class UserAPI(Resource):
    #Resource Fields To Be Converted into JSON Format
    user_fields = {
        'id' : fields.Integer,
        'username': fields.String,
    }

    @marshal_with(user_fields)
    def get(self, user_id):
        res = UserModel.query.filter_by(id=user_id).first()
        print(res)
        if not res:
            abort(404, message = "User can't be found")
        return res

class AccountAPI(Resource):
    #Resource Fields To Be Converted into JSON Format
    account_fields = {
        'id' : fields.Integer,
        'user_id': fields.Integer,
        'acct_type': fields.Integer,
        'balance': fields.Float,
    }

    @marshal_with(account_fields)
    def get(self, account_id):
        res = db.session.query(Account, UserModel, AccountType).filter(Account.id == account_id).all()
        print(res[0].Account)
        if not res:
            abort(404, message = "User can't be found")
        return res[0].Account

api.add_resource(UserAPI, "/user/<int:user_id>")
api.add_resource(AccountAPI, "/account/<int:account_id>")

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=5000, debug=True)
