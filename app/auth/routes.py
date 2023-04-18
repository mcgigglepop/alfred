from app.auth import bp
from flask import request, render_template, redirect, url_for, flash, session, current_app
from flask_login import current_user, logout_user, login_user
from app import db
from app.models import User
import uuid
import random

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route and method for registering a user account. 
    User will redirect to dashboard if they are logged in.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/register.html', title='Register Account')
   
@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route and method for logging in a user account. 
    User will redirect to dashboard if they are logged in.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/login.html', title='Login')
    
@bp.route('/mfa', methods=['GET', 'POST'])
def mfa():
    """
    Route and method for registering the mfa. 
    User will redirect to dashboard if they are logged in.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/mfa.html', title='MFA')