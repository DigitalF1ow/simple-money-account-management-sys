from turtle import reset
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort

# Implement Swagger API
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc

#Config Parser
import configparser

config = configparser.ConfigParser()
config.read('database.ini')

host = config['mariadatabase']['host']
db = config['mariadatabase']['database']
user = config['mariadatabase']['user']
password = config['mariadatabase']['pwd']


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mariadb+pymysql://{user}:{password}@{host}/{db}'


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Money Account Management System',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})

#Setting up with Flask App
docs = FlaskApiSpec(app)
db = SQLAlchemy(app)

#Database Models
class UserModel(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    accounts = db.relationship('AccountModel',backref='user')
    
    #Similar To String Literal in JS
    def __repr__(self):
        return f"User(id={self.id}, user_name={self.user_name})"

class AccountTypeModel(db.Model):
    __tablename__ = 'account_type'
    
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), unique=True, nullable=False)
    accounts = db.relationship('AccountModel',backref='account_type')

    def __repr__(self):
        return f"AccountType(id={self.id},type_name={self.type_name})"

class AccountModel(db.Model):
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    acct_type = db.Column(db.Integer, db.ForeignKey('account_type.id'), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Account(id={self.id},user_id={self.user_id},acct_type={self.acct_type},balance={self.balance})"


#Request Parsers -> Handles Request Parsing
#Automatically Grabs The Request being sent and parse it for the database
account_post_args = reqparse.RequestParser()
account_post_args.add_argument("acct_type", type=int, help="ID of the Account Type is Required!", required=True)
account_post_args.add_argument("user_id", type=int, help="ID of the User is Required!", required=True)
account_post_args.add_argument("balance", type=float, help="Balance of the Account is Required!", required=True)

#Account Update Args
account_put_args = reqparse.RequestParser()
account_put_args.add_argument("transfer_type", type=str)
account_put_args.add_argument("transfer_amount", type=float)


#Schemas used with Marshal With --> Takes results value from database and take into the JSON field, serialize it ino a JSON format
class UserFields(Schema):
    id = fields.Int()
    user_name = fields.Str()

class AccountTypeFields(Schema):
    id = fields.Int()
    type_name = fields.Str()

class AccountFields(Schema):
    id = fields.Int()
    user_id= fields.Int()
    acct_type= fields.Int()
    balance= fields.Float()

@doc(description='Used for Accounts API and AccountsWithUserID API.', tags=['Accounts'])
class AccountWithTypesFields(Schema): 
    id = fields.Int()
    user_id= fields.Int()
    acct_type= fields.Int()
    balance= fields.Float()
    type_name= fields.Str()


class UserAPI(MethodResource, Resource):
    @doc(description='Get for One User.', tags=['User'])
    @marshal_with(UserFields)
    def get(self, user_id):
        res = UserModel.query.filter_by(id=user_id).first()
        print(res)
        if not res:
            abort(404, message = "User can't be found")
        return res

class AccountTypeAPI(MethodResource, Resource):
    @doc(description='Get for One Specific Type.', tags=['Account Types'])
    @marshal_with(AccountTypeFields)
    def get(self, type_id):
        res = AccountModel.query.filter_by(id=type_id).first()
        
        if not res:
            abort(404, message = "Account Type can't be found")
        return res

class AccountTypeListAPI(MethodResource, Resource):
    @doc(description='Get All Types of the Account.', tags=['Account Types'])
    @marshal_with(AccountTypeFields(many=True))
    def get(self):
        res = AccountModel.query.all()
        
        if not res:
            abort(404, message = "Account Types can't be found")
        return res
    
#Individual Account
class AccountAPI(MethodResource, Resource):
    @doc(description='Get One Account By ID.', tags=['Account'])
    @marshal_with(AccountFields)
    def get(self, account_id):
        res = AccountModel.query.filter_by(id=account_id).first()
        
        if not res:
            abort(404, message = "Account can't be found")
        return res
    
    @doc(description='Update using PATCH method to One Account By ID. Has Deduct and Add If Else Logic for Amount Balance', tags=['Account'])
    @marshal_with(AccountFields)
    def patch(self, account_id):
        args = account_put_args.parse_args()

        #Updates only the partial data of the Account
        res = AccountModel.query.filter_by(id=account_id).first()

        if not res:
            abort(404, message="No such Account exist, abort any updates")
        
        #Updates Balance Account based on transfer_type
        if args["transfer_type"] == "deduct":
            if args["transfer_amount"] and (res.balance - args["transfer_amount"]) >= 0: 
                res.balance = res.balance - args["transfer_amount"]
            elif (res.balance - args["transfer_amount"]) < 0:
                abort(400, message="Invalid Amount")

        elif args["transfer_type"] == "add":
            if args["transfer_amount"]: 
                res.balance = res.balance + args["transfer_amount"]
        
        else:
            abort(400, message="Invalid Request, please specify type of transfer")

        #Commits Update
        db.session.commit()

        return res

    @doc(description='Delete One Account', tags=['Account'])
    @marshal_with(AccountFields)
    def delete(self, account_id):
        #Deletes the account instantly
        res = AccountModel.query.filter_by(id=account_id).first()

        if not res:
            abort(404, message="No such Account exist, abort any updates")

        #commits the delete process
        db.session.delete(res)
        db.session.commit()

        return res

#Get All Accounts
class AccountsAPI(MethodResource, Resource):
    @doc(description='Gets all of the accounts from the database including the type names.', tags=['Accounts'])
    @marshal_with(AccountWithTypesFields(many = True))
    def get(self):
        res = AccountModel.query.with_entities(AccountModel.id, AccountModel.user_id, AccountModel.acct_type, AccountModel.balance)\
            .join(AccountTypeModel, AccountModel.acct_type==AccountTypeModel.id)\
            .add_columns(AccountTypeModel.type_name).all()
        if not res:
            abort(404, message = "Accounts can't be found.")
        return res
    
    @doc(description='Creates new account into the database.', tags=['Account'])
    @marshal_with(AccountFields)
    def post(self):
        args = account_post_args.parse_args()
        new_account = AccountModel(user_id=args['user_id'], acct_type=args['acct_type'], balance = args["balance"])
        db.session.add(new_account)
        db.session.commit()
        return new_account, 201

#Get All Accounts Based on User ID
class AccountsByUserID(MethodResource, Resource):
    
    @doc(description='Get Accounts based from a user ID.', tags=['Accounts'])
    @marshal_with(AccountWithTypesFields(many = True))
    def get(self, user_id):
        res = AccountModel.query.with_entities(AccountModel.id, AccountModel.user_id, AccountModel.acct_type, AccountModel.balance)\
            .filter_by(user_id=user_id)\
            .join(AccountTypeModel, AccountModel.acct_type==AccountTypeModel.id)\
            .add_columns(AccountTypeModel.type_name).all()
        print(res)
        
        if not res:
            abort(404, message = "Accounts can't be found.")
        return res


#Users Resource
api.add_resource(UserAPI, "/user/<int:user_id>")

#Account Types Resource
api.add_resource(AccountTypeAPI, "/account-types/<int:type_id>")
api.add_resource(AccountTypeListAPI, "/account-types")

# Accounts API Resource
api.add_resource(AccountsAPI, "/accounts")
api.add_resource(AccountsByUserID, "/accounts/<int:user_id>")
api.add_resource(AccountAPI, "/account/<int:account_id>")

# Register APIs into Swagger UI
docs.register(UserAPI)
docs.register(AccountTypeAPI)
docs.register(AccountTypeListAPI)
docs.register(AccountsByUserID)
docs.register(AccountsAPI)
docs.register(AccountAPI)

@app.route('/')
def index():
    return 'Welcome to Money Account Management System Backend API using Flask Python!'

app.run(host='0.0.0.0', port=5000)
