"""
This module provides utilities for managing database connections using SQLAlchemy.
It defines the database engine, session maker, and base class for declarative models.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Declare the database engine, session maker, and base class for declarative models
engine = create_engine(DATABASE_URL , echo=True)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


#  Dependency function
def get_db():
    """
    This function is used to manage database connections.
    """
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

