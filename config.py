import os

class Config:
    SECRET_KEY = "movieverse14"
    SQLALCHEMY_DATABASE_URI = "sqlite:///movieverse.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False