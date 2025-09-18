import os


SECRET_KEY = os.urandom(32)


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = SECRET_KEY
