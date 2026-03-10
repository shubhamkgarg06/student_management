"""
This module defines the API endpoints for managing subjects in the application. It includes routes for retrieving all subjects, retrieving a subject by ID, and creating a new subject. The endpoints interact with the database through the SubjectCRUD class and utilize
Pydantic schemas for data validation and serialization."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.views.base_crud import BaseCRUD
from app.schemas.subjects import SubjectSchema
from app.models.subjects import SubjectModel
from app.utils.connection_manag import DatabaseManager

# Initialize the API router
router = APIRouter(
    prefix = "/subjects",
    tags = ['subjects']
)



@router.get('/')
def get_subjects(db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve all subject records from the database.
    """
    subject_obj = BaseCRUD(db, SubjectModel)
    return subject_obj.get_all_records()




@router.get('/{id_find}')
def get_subject_by_id(id_find : int, db: Session = Depends(DatabaseManager.get_db)):    
    """
    Retrieve a subject record by its ID.
    """
    subject_obj = BaseCRUD(db, SubjectModel)
    return subject_obj.get_record_by_id(id_find)



@router.post('/')
def add_subject(subject : SubjectSchema, db: Session = Depends(DatabaseManager.get_db)):    
    """
    Create a new subject record in the database.
    """
    subject_obj = BaseCRUD(db, SubjectModel)
    return subject_obj.create_record(subject)


@router.put('/{id_find}')
def update_subject(id_find : int, subject : SubjectSchema, db: Session = Depends(DatabaseManager.get_db)):
    """
    Update an existing subject record in the database.
    """
    subject_obj = BaseCRUD(db, SubjectModel)
    return subject_obj.update_record(id_find, subject)


@router.delete('/{id_del}')
def delete_subject(id_del: int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Delete a subject record from the database.
    """
    subject_obj = BaseCRUD(db, SubjectModel)
    return subject_obj.delete_record(id_del)
