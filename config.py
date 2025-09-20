import os
from urllib.parse import urlparse

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')
    DATABASE_URL = os.environ.get('DATABASE_URL') 
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///shopeasy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
