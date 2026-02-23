"""
This module defines the Pydantic model for a section in the school management system.
"""
from pydantic import BaseModel


class SectionSchema(BaseModel):
    """
    Pydantic model for a section in the school management system.
    """
    id : int
    section_name : str
