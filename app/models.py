from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    passwordHash = db.Column(db.String(128))
    registeredDate = db.Column(db.DateTime, default=datetime.utcnow)
    accountType = db.Column(db.String(64), default='free')
    accounts = db.relationship('DepositAccount', backref='author', lazy='dynamic')

     
    def __repr__(self):
        return '<User {}>'.format(self.email)

    def setPassword(self, password):
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)

    def getEmail(self):
        return self.email
        
    def getName(self):
        return f'{self.firstName} {self.lastName}'

class DepositAccount(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accountName = db.Column(db.String(128))
    accountType = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<DepositAccount {}>'.format(self.accountName)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))