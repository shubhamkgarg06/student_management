"""
This module defines the StudentModel class, which represents the students table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.connection_manag import Base
from app.models.base import DBBase


class StudentModel(Base, DBBase):
    """
    This class represents the students table in the database.
    This table is connected to the sections table using a foreign key relationship.
    It consists of columns for id, name, father's name, age, and section_id.
    The id column is the primary key, while the section_id column is a foreign key that references the sections table.
    It also has a relationship with the SectionModel class, allowing us to access the section information for each student.
    """


    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    father_name = Column(String)
    age = Column(Integer)

    # This is the foreign key column that references the sections table
    # Combination of student id and section id is primary key because a student can be in multiple sections but only once in each section
    section_id = Column(Integer, ForeignKey('sections.id') , primary_key=True)

    # Link back to section
    # This creates a relationship between the StudentModel and SectionModel classes, allowing us to access the section information for each student.
    section = relationship("SectionModel", back_populates="students")

    # This creates a relationship between the StudentModel and MidtermMarksModel classes, allowing us to access the marks for each student.
    # This is a parent model to the MidtermMarksModel class, which means that when a student is deleted, all the marks associated with that student will also be deleted.
    marks = relationship(
        "MidtermMarksModel",
        back_populates="student",
        cascade="all, delete-orphan"
    )
