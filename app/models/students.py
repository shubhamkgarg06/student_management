"""
This module defines the StudentModel class, which represents the students table in the database.
"""
from sqlalchemy import Column, Integer, String
from app.utils.connection_manag import Base
from app.models.base import DBBase


class StudentModel(Base, DBBase):
    """
    This class represents the students table in the database.
    """
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    father_name = Column(String)
    age = Column(Integer)
