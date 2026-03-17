"""
This module defines the API routes for user authentication, including login and registration. It uses FastAPI's APIRouter to create endpoints under the "/auth" prefix. The router includes two POST endpoints: "/login" for user login and "/register" for user registration. Both endpoints depend on a database session provided by the DatabaseManager. The AuthController is used to handle the logic for both operations, interacting with the database as needed.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import UserLogin , UserCreate
from app.utils.connection_manag import DatabaseManager
from app.views.auth import AuthController

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(DatabaseManager.get_db)):
    """
    Authenticates a user by verifying their credentials and generating a JWT token.
    :param data: A UserLogin schema containing the username and password.
    :param db: A database session provided by the DatabaseManager.
    :return: A dictionary containing the access token if authentication is successful.
    """

    data = UserLogin(
        username=form_data.username,
        password=form_data.password
    )
    auth_controller = AuthController(db)
    # print(data)
    return auth_controller.login(data)
    


@router.post("/register")
def register(data: UserCreate, db: Session = Depends(DatabaseManager.get_db)):

    """
    Registers a new user by creating a user record with a hashed password.
    :param data: A UserCreate schema containing the username, password, and role for the new user.
    :param db: A database session provided by the DatabaseManager.
    :return: A message indicating the result of the registration process.
    """
    auth_controller = AuthController(db)
    return auth_controller.register(data)