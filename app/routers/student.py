"""
This module defines the API routes for managing student data in the application. 
It uses FastAPI's APIRouter to create endpoints for CRUD operations on student records. 
It includes routes for retrieving all students, getting a student by ID, getting students by section ID, 
creating a new student, updating an existing student, deleting a student, and partially updating a student's data
"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.views.student import StudentCRUD
from app.views.base_crud import BaseCRUD
from app.schemas.student import StudentSchema , StudentPatchSchema
from app.models.students import StudentModel
from app.utils.connection_manag import DatabaseManager



# Initialize the API router
router = APIRouter(
    prefix = "/students",
    tags = ['students']
)



@router.get('/')
def get_students(db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve all student records from the database.
    """
    stud_obj = BaseCRUD(db ,StudentModel)
    return stud_obj.get_all_records()



@router.get('/{id_find}')
def get_std_id(id_find : int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve a student record by its ID.
    """
    student_obj =BaseCRUD(db , StudentModel)
    return student_obj.get_record_by_id(id_find)



@router.get('/section/{section_id_find}')
def get_std_by_section_id(section_id_find : int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Retrieve all students in a specific section.
    """
    student_obj = StudentCRUD(db)
    return student_obj.get_student_by_section_id(section_id_find)



@router.post('/')
def add_student(std : StudentSchema, db: Session = Depends(DatabaseManager.get_db)):
    """
    Create a new student record in the database.
    """
    student_obj = StudentCRUD(db)
    return student_obj.create_student(std)



@router.put('/{id_up}/{section_id_up}')
def update_student(id_up : int , section_id_up : int, std_data : StudentSchema, db: Session = Depends(DatabaseManager.get_db)):
    """
    Update an existing student record in the database.
    """
    student_obj = StudentCRUD(db)
    return student_obj.update_student(id_up , section_id_up , std_data)



@router.delete('/{id_del}/{section_id_del}')
def delete_std_data(id_del : int, section_id_del : int, db: Session = Depends(DatabaseManager.get_db)):
    """
    Delete a student record from the database.
    """
    student_obj = StudentCRUD(db)
    return student_obj.delete_student_record(id_del , section_id_del)



@router.patch('/{id_patch}')
def patch_student_data(
        id_patch : int,
        student: StudentPatchSchema,
        db : Session = Depends(DatabaseManager.get_db)
    ):

    """
    Partially update a students data
    """

    student_obj = StudentCRUD(db)
    return student_obj.patch_student_data(id_patch , student)
