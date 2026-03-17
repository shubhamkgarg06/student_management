"""
This module defines the UserModel class, which represents the users table in the database. It uses SQLAlchemy's declarative base to define the structure of the table, including columns for id, username, password, and role. The UserModel class inherits from DatabaseManager.Base, allowing it to be used with SQLAlchemy's ORM features for database interactions.
"""
from sqlalchemy import Column, Integer, String
from app.utils.connection_manag import DatabaseManager

class UserModel(DatabaseManager.Base):

    """
    This class represents the users table in the database. It uses SQLAlchemy's declarative base to define the structure of the table, including columns for id, username, password, and role. The UserModel class inherits from DatabaseManager.Base, allowing it to be used with SQLAlchemy's ORM features for database interactions.
    The id column is the primary key, while the username column is unique to ensure that no two users can have the same username. The password column stores the hashed password of the user, and the role column indicates the user's role (e.g., admin, student, etc.).
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)