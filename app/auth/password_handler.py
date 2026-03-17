"""
This module defines the functions for hashing and verifying passwords using the Passlib library. The hash_password function takes a plain text password as input and returns a hashed version of it using the bcrypt algorithm. The verify_password function takes a plain text password and a hashed password as input and returns a boolean indicating whether the plain text password matches the hashed password. These functions are essential for securely storing user passwords and validating user credentials during authentication.
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """
    Hashes a plain text password using the bcrypt algorithm.
    """
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str):
    """
    Verifies a plain text password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)