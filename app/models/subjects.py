"""
This module defines the SubjectModel class, which represents the subjects table in the database.
"""
from sqlalchemy import Column, Integer, String
from app.utils.connection_manag import Base
from app.models.base import DBBase

class SubjectModel(Base , DBBase):

    """
    This class represents the subjects table in the database.
    It consist two columns id and subject_name. 
    The id column is the primary key and subject_name column stores the name of the subject.
    """

    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)

