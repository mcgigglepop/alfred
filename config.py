import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') or ''
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') or ''
    REGION_NAME = os.environ.get('REGION_NAME') or 'us-east-2'
    SECRETS_BUCKET = os.environ.get('SECRETS_BUCKET') or ''
    KMS_KEY_ALIAS = os.environ.get('KMS_KEY_ALIAS') or ''