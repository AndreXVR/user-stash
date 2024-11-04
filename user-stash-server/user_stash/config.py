from os import environ
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)


class Config:
    SECRET_KEY = environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("FLASK_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
