"""
This module defines the API endpoints for managing midterm marks in the student management system.
It includes routes for creating new midterm marks records, retrieving all midterm marks, and searching for midterm marks based on specific criteria such as student ID, subject ID, or section ID. The endpoints interact with the database through the MidTermMarksCRUD class, which handles the business logic for managing midterm marks data.
"""

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.views.MidTermMarks import MidTermMarksCRUD
from app.schemas.MidTermMarks import MidTermMarksSchema
from app.utils.connection_manag import get_db


# Initialize the API router
router = APIRouter(
    prefix = "/marks",
    tags = ['marks']
)

@router.post('/marks/')
def add_marks(marks : MidTermMarksSchema, db: Session = Depends(get_db)):
    """
    Create a new midterm marks record in the database.
    """
    marks_obj = MidTermMarksCRUD(db)
    return marks_obj.create_midterm_marks(marks)    


@router.get('/marks/')
def get_marks(db: Session = Depends(get_db)):
    """
    Retrieve all midterm marks records from the database.
    """
    marks_obj = MidTermMarksCRUD(db)
    return marks_obj.get_marks_table_data() 

@router.get('/marks/search')
def get_marks_by_criteria(student_id: int = None, subject_id: int = None, section_id: int = None, db: Session = Depends(get_db)):
    """
    Retrieve midterm marks records based on specific criteria such as student ID, subject ID, or section ID.
    """
    marks_obj = MidTermMarksCRUD(db)
    return marks_obj.get_marks_by_specific_criteria(student_id, subject_id, section_id)