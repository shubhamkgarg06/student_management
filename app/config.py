"""
Configuration file for the application. 
It loads environment variables and constructs the database URL.
"""
import os
from dotenv import load_dotenv


load_dotenv()  # loads variables from .env

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")


# Construct the database URL for SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
