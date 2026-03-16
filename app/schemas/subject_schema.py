"""
This file defines the Pydantic schema for the Subject model.
The SubjectSchema class is a Pydantic model that represents the structure of the data for a subject.
It has two fields: subject_id and subject_name, which correspond to the columns in the subjects table in the database.
"""
from pydantic import BaseModel

class SubjectSchema(BaseModel):
    """This class represents the schema for the Subject model."""
    subject_id : int
    subject_name : str
