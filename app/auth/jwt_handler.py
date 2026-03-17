"""
This module defines the function for creating JWT access tokens for user authentication. The create_access_token function takes a dictionary of data as input, adds an expiration time to it, and encodes it into a JWT token using the specified secret key and algorithm. The resulting token can be used for authenticating users in the application, allowing them to access protected resources based on their credentials and permissions.
"""

from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict):

    """
    Creates a JWT access token with the provided data and an expiration time of 1 hour.
    :param data: A dictionary containing the data to be included in the token payload.
    :return: A JWT token as a string.
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token