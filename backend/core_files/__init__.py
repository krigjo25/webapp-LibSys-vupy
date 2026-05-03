#   Core configuration of the Flask application

# Importing the required libraries
from flask import Flask
from flask_cors import CORS # type: ignore (Library lacks type stubs)
from flask_session import Session # type: ignore (Library lacks type stubs)
from flask_sqlalchemy import SQLAlchemy

from lib.config.log_config import AppWatcher
from lib.config.env_config import settings

#   Initialize logger configurations
logger = AppWatcher()
logger.FileHandler() # type: ignore (Library lacks type stubs in base class Log)

#   Initialize the Flask application
app = Flask(__name__)
# Load configuration from Pydantic settings object
app.config.from_mapping(settings.model_dump())

#   Initialize the database connection
db = SQLAlchemy(app)

#   Initialize the session
Session(app) # type: ignore (Library lacks type stubs)

#   CORS Configurations
cors_origins = settings.LOCAL_ORIGINS if settings.DEBUG else settings.CORS_ORIGINS
CORS(app, resources={r"/.*": {"origins": {cors_origins}}}) # type: ignore (Library lacks type stubs)

#   Log the application configurations
logger.info('Application Configurations START') # type: ignore (Library lacks type stubs in base class Log)
