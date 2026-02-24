"""
This module defines the SectionModel class, which represents the sections table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.connection_manag import Base
from app.models.base import DBBase

class SectionModel(Base , DBBase):

    """
    This class represents the section table in the database.
    This table is connected to student table using relationship.
    It consist two columns id and section_name. 
    The id column is the primary key and section_name column stores the name of the section.
    It also has a relationship with the StudentModel class, allowing us to access the students in each section.
    """

    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    section_name = Column(String)

    # This creates a relationship between the SectionModel and StudentModel classes, allowing us to access the students in each section.
    students = relationship(
        "StudentModel",          # name of the related class
        back_populates="section",  # link to the attribute in the child class
        cascade="all, delete-orphan"  # optional, what happens when parent is deleted
    )

    # This creates a relationship between the SectionModel and MidtermMarksModel classes, allowing us to access the marks for each section.
    # This is a parent model to the MidtermMarksModel class, which means that when a section is deleted, all the marks associated with that section will also be deleted.
    
    marks = relationship(
        "MidtermMarksModel",
        back_populates="section",
        cascade="all, delete-orphan"
    )
