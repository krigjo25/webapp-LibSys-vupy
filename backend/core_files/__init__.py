#   Core configuration of the Flask application

# Importing the required libraries
import os

from flask import Flask
from flask_cors import CORS # type: ignore (Library lacks type stubs)
from dotenv import load_dotenv
from flask_session import Session # type: ignore (Library lacks type stubs)
from flask_sqlalchemy import SQLAlchemy

from lib.config.log_config import AppWatcher
from lib.config.env_config import DevelopmentConfig

#   Load the environment variables from the .env file
load_dotenv()

#   Initialize logger configurations
logger = AppWatcher()
logger.FileHandler() # type: ignore (Library lacks type stubs in base class Log)

#   Initialize the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

#   Initialize the database connection
db = SQLAlchemy(app)

#   Initialize the session
Session(app) # type: ignore (Library lacks type stubs)

#   CORS Configurations
CORS_ORIGINS = os.getenv('Local_ORIGINS') if app.config['DEBUG'] else os.getenv('CORS_ORIGINS')
CORS(app, resources={r"/.*": {"origins": {CORS_ORIGINS}}}) # type: ignore (Library lacks type stubs)

#   Log the application configurations
logger.info('Application Configurations START') # type: ignore (Library lacks type stubs in base class Log)
