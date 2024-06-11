import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///cats.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    CAT_API_URL = 'https://api.thecatapi.com/v1'
    CAT_API_KEY = os.getenv('CAT_API_KEY')
