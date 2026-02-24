"""
This module defines the SubjectModel class, which represents the subjects table in the database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
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

    # This creates a relationship between the SubjectModel and MidtermMarksModel classes, allowing us to access the marks of each subject.
    # It is a parent model to the MidtermMarksModel class, which means that when a subject is deleted, all the marks associated with that subject will also be deleted.
    marks = relationship(
        "MidtermMarksModel",
        back_populates="subject",
        cascade="all, delete-orphan"
    )

