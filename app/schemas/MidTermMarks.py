"""
This module defines the Pydantic models for the midterm marks.
 These models are used to validate and serialize the data for the midterm marks when it is sent to or received from the API endpoints.
"""

from pydantic import BaseModel


class MidTermMarksSchema(BaseModel):
    """
    Pydantic model for the midterm marks.
    """

    student_id : int
    subject_id : int
    section_id : int
    marks : int