"""
This module provides utilities for managing database connections using SQLAlchemy.
It defines the database engine, session maker, and base class for declarative models.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL , echo=True)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
