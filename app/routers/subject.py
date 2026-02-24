"""
This module defines the API endpoints for managing subjects in the application. It includes routes for retrieving all subjects, retrieving a subject by ID, and creating a new subject. The endpoints interact with the database through the SubjectCRUD class and utilize
Pydantic schemas for data validation and serialization."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.views.subject import SubjectCRUD
from app.schemas.subjects import SubjectSchema
from app.utils.connection_manag import get_db

# Initialize the API router
router = APIRouter(
    prefix = "/subjects",
    tags = ['subjects']
)



@router.get('/subjects/')
def get_subjects(db: Session = Depends(get_db)):
    """
    Retrieve all subject records from the database.
    """
    subject_obj = SubjectCRUD(db)
    return subject_obj.get_all_subjects()




@router.get('/subjects/{id_find}')
def get_subject_by_id(id_find : int, db: Session = Depends(get_db)):    
    """
    Retrieve a subject record by its ID.
    """
    subject_obj = SubjectCRUD(db)
    return subject_obj.get_subject_by_id(id_find)



@router.post('/subjects/')
def add_subject(subject : SubjectSchema, db: Session = Depends(get_db)):    
    """
    Create a new subject record in the database.
    """
    subject_obj = SubjectCRUD(db)
    return subject_obj.create_subject(subject)

@router.put('/subjects/{id_find}')
def update_subject(id_find : int, subject : SubjectSchema, db: Session = Depends(get_db)):
    """
    Update an existing subject record in the database.
    """
    subject_obj = SubjectCRUD(db)
    return subject_obj.update_subject(id_find, subject)
