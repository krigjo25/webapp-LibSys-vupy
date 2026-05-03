from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    # Flask Settings
    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = "default-secret-key"
    
    # Session Settings
    SESSION_TYPE: str = 'filesystem'
    SESSION_PERMANENT: bool = False
    
    # Database Settings
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///test.db"
    
    # Custom Origins
    CORS_ORIGINS: str = "*"
    LOCAL_ORIGINS: str = "http://localhost:5173"

    # Database connection details (for MariaDB utility)
    H0ST: str = "localhost"
    MASTER: str = "root"
    PORT: int = 3306
    PASSWORD: str = ""
    DATABASE: str = "library"
    DATABASE7: str = ""

settings = Settings()
