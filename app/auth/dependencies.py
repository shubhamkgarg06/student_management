"""
This module defines the dependencies for user authentication and authorization in the FastAPI application.
It includes functions to retrieve the current user based on the JWT token provided in the request and to enforce admin-only access to certain endpoints. The get_current_user function decodes the JWT token to extract user information, while the admin_only function checks if the user's role is "admin" and raises an HTTPException if they are not authorized to access the resource.
"""
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the JWT token provided in the request.
    :param token: The JWT token extracted from the request's Authorization header.
    :return: A dictionary containing the user's information if the token is valid.
    :raises HTTPException: If the token is invalid or cannot be decoded.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Decoded JWT payload:", payload)  # Debugging statement

        username: str = payload.get("username")
        role = payload.get("role")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    


def admin_only(user: dict = Depends(get_current_user)):
    """
    Enforces admin-only access to certain endpoints by checking the user's role.
    :param user: A dictionary containing the user's information, obtained from the get_current_user dependency
    :return: The user information if the user is an admin.
    :raises HTTPException: If the user is not an admin.
    """
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user