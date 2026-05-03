from flask import Flask
from flask_cors import CORS # type: ignore (Library lacks type stubs)
from flask_session import Session # type: ignore (Library lacks type stubs)
from flask_sqlalchemy import SQLAlchemy

from lib.config.log_config import AppWatcher
from lib.config.env_config import settings

logger = AppWatcher()
logger.file_handler() # type: ignore (Library lacks type stubs in base class Log)

app = Flask(__name__)
app.config.from_mapping(settings.model_dump())

db = SQLAlchemy(app)
Session(app) # type: ignore (Library lacks type stubs)

cors_origins = settings.LOCAL_ORIGINS if settings.DEBUG else settings.CORS_ORIGINS
CORS(app, resources={r"/.*": {"origins": {cors_origins}}}) # type: ignore (Library lacks type stubs)

logger.info('Application Configurations START') # type: ignore (Library lacks type stubs in base class Log)
