"""
This module defines API endpoints for managing sections in the student management system.
It consists API routes for getting all sections, getting a section by ID, creating a new section,
 and retrieving students by section name.
"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.views.section import SectionCRUD
from app.schemas.section import SectionSchema
from app.utils.connection_manag import get_db

# Initialize the API router
router = APIRouter(
    prefix = "/sections",
    tags = ['sections']
)

@router.get('/sections/')
def get_sections(db: Session = Depends(get_db)):
    """
    Retrieve all section records from the database.
    """
    section_obj = SectionCRUD(db)
    return section_obj.get_all_sections()           


@router.get('/sections/{id_find}')
def get_section_by_id(id_find : int, db: Session = Depends(get_db)):
    """
    Retrieve a section record by its ID.
    """
    section_obj = SectionCRUD(db)
    return section_obj.get_section_by_id(id_find)


@router.post('/sections/')
def add_section(section : SectionSchema, db: Session = Depends(get_db)):    
    """
    Create a new section record in the database.
    """
    section_obj = SectionCRUD(db)
    return section_obj.create_section(section)  



@router.put('/sections/{id_update}')
def update_section(id_update: int, section: SectionSchema, db: Session = Depends(get_db)):
    """
    Update a section record in the database.
    """
    section_obj = SectionCRUD(db)
    return section_obj.update_section(id_update, section)



@router.get('/sections/{section_name}/students')
def get_students_by_section_name(section_name: str, db: Session = Depends(get_db)):
    """
    Retrieve all students in a specific section by section name.
    """
    section_obj = SectionCRUD(db)
    return section_obj.get_students_by_section_name(section_name)

