import os

from dotenv import load_dotenv


load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')
