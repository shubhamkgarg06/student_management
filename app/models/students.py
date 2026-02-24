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
    """


    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    father_name = Column(String)
    age = Column(Integer)
    section_id = Column(Integer, ForeignKey('sections.id'))

    # Link back to section
    section = relationship("SectionModel", back_populates="students")
