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
    This table is connected to student table using relationship
    """

    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    section_name = Column(String)

    students = relationship(
        "Student",          # name of the related class
        back_populates="section",  # link to the attribute in the child class
        cascade="all, delete-orphan"  # optional, what happens when parent is deleted
    )
