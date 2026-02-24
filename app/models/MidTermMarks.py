"""
This module defines the MidTermMarksModel, which represents marks of different students in different subjects.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.connection_manag import Base
from app.models.base import DBBase

class MidTermMarksModel(Base , DBBase):

    """
    This class represents the midterm marks of students in different subjects.
    It consists of columns for student_id, subject_id, section_id and marks.
    The combination of student_id, subject_id and section_id is the primary key, which means that a student can have only one mark for a specific subject in a specific section.
    It also has relationships with the StudentModel, SubjectModel and SectionModel classes, allowing us to access the student, subject and section information for each mark.
    This is a child model to the StudentModel, SubjectModel and SectionModel classes, which means that when a student, subject or section is deleted, all the marks associated with that student, subject or section will also be deleted.
    """

    __tablename__ = 'midterm_marks'

    student_id = Column(Integer , ForeignKey('students.id') , primary_key = True)
    subject_id = Column(Integer , ForeignKey('subjects.subject_id') , primary_key = True)
    section_id = Column(Integer , ForeignKey('sections.id') , primary_key = True)
    marks = Column(Integer)


    # This creates a relationship between the MidtermMarksModel and SubjectModel classes, allowing us to access the subject information for each mark.
    # This is a child model to the SubjectModel class, which means that when a subject is deleted, all the marks associated with that subject will also be deleted.
    subject = relationship("SubjectModel" , back_populates="marks")
    section = relationship("SectionModel" , back_populates="marks")
    student = relationship("StudentModel" , back_populates="marks")

