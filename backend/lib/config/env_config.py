#   Configuration settings for the app

#   Importing the required modules
import os

class DefaultConfig(object):
    # ...
    # The default configuration for the app
    # ...
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///')
    

class DevelopmentConfig(DefaultConfig):
    # ...
    # The development configuration for the app
    # ...
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"