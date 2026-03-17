"""
This module defines the AuthController class, which handles user authentication and registration.
It uses SQLAlchemy for database interactions, and includes methods for logging in and registering users. 
The login method verifies user credentials and generates a JWT token, while the register method creates a new user with a hashed password.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserLogin , UserCreate
from app.models.user_model import UserModel
from app.auth.password_handler import hash_password
from app.auth.password_handler import verify_password
from app.auth.jwt_handler import create_access_token



class AuthController:

    """
    This class handles user authentication and registration.
    It uses SQLAlchemy for database interactions, and includes methods for logging in and registering users.
    The login method verifies user credentials and generates a JWT token, while the register method creates a new user with a hashed password.
    """


    def __init__(self, db: Session):
        """
        Initializes the AuthController instance with a database session.
        """
        self.db = db



    def login(self, data: UserLogin):
        """
        Authenticates a user by verifying their credentials and generating a JWT token.
        :param data: A UserLogin schema containing the username and password.
        """

        user = self.db.query(UserModel).filter(UserModel.username == data.username).first()

        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({
            "username": user.username,
            "role": user.role
        })

        return {"access_token": token}
    


    def register(self, data: UserCreate):
        """
        Registers a new user by creating a user record with a hashed password.
        :param data: A UserCreate schema containing the username, password, and role for the new user."""

        existing_user = self.db.query(UserModel).filter(UserModel.username == data.username).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_password = hash_password(data.password)

        #  Create user object
        new_user = UserModel(
            username=data.username,
            password=hashed_password,
            role=data.role
        )

        #  Save to DB
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return {"message": "User created successfully"}
