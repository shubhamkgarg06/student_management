"""
This module defines the API routes for managing student data in the application. 
It uses FastAPI's APIRouter to create endpoints for CRUD operations on student records. 
"""
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.views.student import StudentCRUD
from app.schemas.student import StudentSchema , StudentPatchSchema
from app.utils.connection_manag import get_db



# Initialize the API router
router = APIRouter()

@router.get('/')
def home():
    """
    Home endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Student API!"}

@router.get('/students/')
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve all student records from the database.
    """
    stud_obj = StudentCRUD(db)
    return stud_obj.get_all_students()


@router.get('/students/{id_find}')
def get_std_id(id_find : int, db: Session = Depends(get_db)):
    """
    Retrieve a student record by its ID.
    """
    stud_obj = StudentCRUD(db)
    return stud_obj.get_student_by_id(id_find)


@router.post('/students/')
def add_student(std : StudentSchema, db: Session = Depends(get_db)):
    """
    Create a new student record in the database.
    """
    stud_obj = StudentCRUD(db)
    return stud_obj.create_student(std)



@router.put('/students/{id_up}')
def update_student(id_up : int , std_data : StudentSchema, db: Session = Depends(get_db)):
    """
    Update an existing student record in the database.
    """
    stud_obj = StudentCRUD(db)
    return stud_obj.update_student_data(id_up , std_data)



@router.delete('/students/{id_del}')
def delete_std_data(id_del : int, db: Session = Depends(get_db)):
    """
    Delete a student record from the database.
    """
    stud_obj = StudentCRUD(db)
    return stud_obj.delete_student(id_del)



@router.patch('/students/{id_patch}')
def patch_student_data(
        id_patch : int , 
        student: StudentPatchSchema , 
        db : Session = Depends(get_db)
    ):

    """
    Partially update a students data
    """

    stud_obj = StudentCRUD(db)
    return stud_obj.patch_student_data(id_patch , student)

