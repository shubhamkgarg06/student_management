"""
This module defines the Pydantic models for user authentication and registration. It includes two classes: UserLogin and UserCreate. The UserLogin class is used for validating the data received during user login, containing fields for username and password. The UserCreate class is used for validating the data received during user registration, containing fields for username, password, and role. These models ensure that the incoming data adheres to the expected structure and types before being processed by the authentication logic in the AuthController.
"""
from pydantic import BaseModel

class UserLogin(BaseModel):
    """
    This class is a Pydantic model that defines the structure of the data required for user login. It contains two fields: username and password, both of which are of type string. This model is used to validate the incoming data when a user attempts to log in, ensuring that the necessary information is provided and is in the correct format.
    """
    username: str
    password: str

class UserCreate(BaseModel):
    """
    This class is a Pydantic model that defines the structure of the data required for user registration. It contains three fields: username, password, and role, all of which are of type string. This model is used to validate the incoming data when a new user attempts to register, ensuring that the necessary information is provided and is in the correct format. The role field indicates the user's role (e.g., admin, student, etc.) and is essential for determining the user's permissions within the system.
    """
    username: str
    password: str
    role: str