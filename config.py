import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CLIENT_LOGGING_LEVEL = os.getenv("CLIENT_LOGGING_LEVEL")
    CLIENT_LOGGING_FILE = os.getenv("CLIENT_LOGGING_FILE")
    CLIENT_SERVER_HOST = os.getenv("CLIENT_SERVER_HOST")
    CLIENT_SERVER_PORT = os.getenv("CLIENT_SERVER_PORT")
    CLIENT_DEBUG = os.getenv("CLIENT_DEBUG")
    REST_LOGGING_LEVEL = os.getenv("REST_LOGGING_LEVEL")
    REST_LOGGING_FILE = os.getenv("REST_LOGGING_FILE")
    REST_SERVER_HOST = os.getenv("REST_SERVER_HOST")
    REST_SERVER_PORT = os.getenv("REST_SERVER_PORT")
    REST_DEBUG = os.getenv("REST_DEBUG")
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_DATABASE = os.getenv('DB_DATABASE')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
