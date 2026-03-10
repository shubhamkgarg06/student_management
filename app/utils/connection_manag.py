"""
This module provides utilities for managing database connections using SQLAlchemy.
It defines the database engine, session maker, and base class for declarative models.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL


class DatabaseManager:

    """
        This class manages the database connection and session creation.
        It provides a method to get a database session, ensuring proper handling of transactions.
    """

    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base = declarative_base()

    @classmethod
    def get_db(cls):
        """
        This function manages database connections.
        """
        db = cls.SessionLocal()

        try:
            yield db
            db.commit()

        except:
            db.rollback()
            raise

        finally:
            db.close()
