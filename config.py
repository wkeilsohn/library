import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'So-many-books-so-little-time'