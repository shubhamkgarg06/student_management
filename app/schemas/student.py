"""
This module defines the Pydantic model for a student in the school management system. 
The model includes fields for the student's ID, name, father's name, and age.
"""
from pydantic import BaseModel
from typing import Optional


class StudentSchema(BaseModel):
    """
    Pydantic model for a student in the school management system.
    """
    id : int
    name : str
    father_name : str
    age : int


class StudentPatchSchema(BaseModel):
    """
    Pydantic model for updating student information in the school management system.
    All fields are optional to allow partial updates.
    """
    name: Optional[str] = None
    father_name: Optional[str] = None
    age: Optional[int] = None
