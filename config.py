import os


DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Forever98'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'demo'

DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False