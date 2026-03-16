"""
This module defines API endpoints for managing sections in the student management system.
It consists API routes for getting all sections, getting a section by ID, creating a new section,
 and retrieving students by section name.
"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.views.section import SectionCRUD
from app.views.base_crud import BaseCRUD
from app.schemas.section_schema import SectionSchema
from app.models.section_model import SectionModel
from app.utils.connection_manag import DatabaseManager

# Initialize the API router
router = APIRouter(
    prefix = "/sections",
    tags = ['sections']
)

@router.get('/')
def get_sections(db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve all section records from the database.
    """
    section_obj = BaseCRUD(db, SectionModel)
    return section_obj.get_all_records()


@router.get('/{id_find}')
def get_section_by_id(id_find : int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve a section record by its ID.
    """
    section_obj = BaseCRUD(db, SectionModel)
    return section_obj.get_record_by_id(id_find)


@router.post('/')
def add_section(section : SectionSchema, db: Session = Depends(DatabaseManager.get_db)):    
    """
    Create a new section record in the database.
    """
    section_obj = BaseCRUD(db, SectionModel)
    return section_obj.create_record(section)



@router.put('/{id_update}')
def update_section(id_update: int, section: SectionSchema, db: Session = Depends(DatabaseManager.get_db)):
    """
    Update a section record in the database.
    """
    section_obj = BaseCRUD(db, SectionModel)
    return section_obj.update_record(id_update, section)



@router.get('/{section_name}/students')
def get_students_by_section_name(section_name: str, db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve all students in a specific section by section name.
    """
    section_obj = SectionCRUD(db)
    return section_obj.get_students_by_section_name(section_name)


@router.delete('/{id_delete}')
def delete_section(id_delete: int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Delete a section record from the database.
    """
    section_obj = BaseCRUD(db, SectionModel)
    return section_obj.delete_record(id_delete)


