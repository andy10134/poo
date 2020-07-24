import os

SECRET_KEY = 'GDtfDCFYjD'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.abspath(os.getcwd()) +'/data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False