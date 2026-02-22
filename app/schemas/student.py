"""
This module defines the Pydantic model for a student in the school management system. 
The model includes fields for the student's ID, name, father's name, and age.
"""
from pydantic import BaseModel


class StudentSchema(BaseModel):
    """
    Pydantic model for a student in the school management system.
    """
    id : int
    name : str
    father_name : str
    age : int
