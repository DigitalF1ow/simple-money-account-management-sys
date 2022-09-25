from turtle import reset
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
    accounts = db.relationship('AccountModel',backref='user')
    
    #Similar To String Literal in JS
    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

class AccountTypeModel(db.Model):
    __tablename__ = 'account_type'
    
    id = db.Column(db.Integer, primary_key=True)
    typename = db.Column(db.String(255), unique=True, nullable=False)
    accounts = db.relationship('AccountModel',backref='account_type')

    def __repr__(self):
        return f"AccountType(id={self.id},typename={self.typename})"

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


#Serializers with Marshal With --> Takes results value from database and take into the JSON field, serialize it ino a JSON format
user_fields = {
    'id' : fields.Integer,
    'username': fields.String,
}

acctType_fields = {
    'id' : fields.Integer,
    'typename': fields.String,
}

account_fields = {
    'id' : fields.Integer,
    'user_id': fields.Integer,
    'acct_type': fields.Integer,
    'balance': fields.Float,
}

account_with_types_fields = {
    'id' : fields.Integer,
    'user_id': fields.Integer,
    'acct_type': fields.Integer,
    'balance': fields.Float,
    'typename': fields.String,
}


class UserAPI(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        res = UserModel.query.filter_by(id=user_id).first()
        
        if not res:
            abort(404, message = "User can't be found")
        return res

class AccountTypeAPI(Resource):
    @marshal_with(acctType_fields)
    def get(self, type_id):
        res = AccountModel.query.filter_by(id=type_id).first()
        
        if not res:
            abort(404, message = "Account Type can't be found")
        return res
    

#Individual Account
class AccountAPI(Resource):

    @marshal_with(account_fields)
    def get(self, account_id):
        res = AccountModel.query.filter_by(id=account_id).first()
        
        if not res:
            abort(404, message = "Account can't be found")
        return res
    
    @marshal_with(account_fields)
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

    @marshal_with(account_fields)
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
class AccountsAPI(Resource):
    @marshal_with(account_with_types_fields)
    def get(self):
        res = AccountModel.query.with_entities(AccountModel.id, AccountModel.user_id, AccountModel.acct_type, AccountModel.balance)\
            .join(AccountTypeModel, AccountModel.acct_type==AccountTypeModel.id)\
            .add_columns(AccountTypeModel.typename).all()
        if not res:
            abort(404, message = "Accounts can't be found.")
        return res

    @marshal_with(account_fields)
    def post(self):
        args = account_post_args.parse_args()
        new_account = AccountModel(user_id=args['user_id'], acct_type=args['acct_type'], balance = args["balance"])
        db.session.add(new_account)
        db.session.commit()
        return new_account, 201

#Get All Accounts Based on User ID
class AccountsByUserID(Resource):

    @marshal_with(account_with_types_fields)
    def get(self, user_id):
        res = AccountModel.query.with_entities(AccountModel.id, AccountModel.user_id, AccountModel.acct_type, AccountModel.balance)\
            .filter_by(user_id=user_id)\
            .join(AccountTypeModel, AccountModel.acct_type==AccountTypeModel.id)\
            .add_columns(AccountTypeModel.typename).all()
        print(res)
        
        if not res:
            abort(404, message = "Accounts can't be found.")
        return res


#Users Resource
api.add_resource(UserAPI, "/user/<int:user_id>")

#Account Types Resource

# Accounts API Resource

api.add_resource(AccountsAPI, "/accounts")
api.add_resource(AccountsByUserID, "/accounts/<int:user_id>")
api.add_resource(AccountAPI, "/account/<int:account_id>")

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=5000, debug=True)
