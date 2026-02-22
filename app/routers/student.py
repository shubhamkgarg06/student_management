"""
This module defines the API routes for managing student data in the application. 
It uses FastAPI's APIRouter to create endpoints for CRUD operations on student records. 
"""
from fastapi import APIRouter
from app.views.student import StudentCRUD
from app.schemas.student import StudentSchema



# Initialize the API router
router = APIRouter()


# Creates a StudentCRUD object to handle student data operations
stud_obj = StudentCRUD()



@router.get('/students/')
def get_students():
    """
    Retrieve all student records from the database.
    """
    return stud_obj.get_all_students()


@router.get('/students/{id_find}')
def get_std_id(id_find : int):
    """
    Retrieve a student record by its ID.
    """
    return stud_obj.get_student_by_id(id_find)


@router.post('/students/')
def add_student(std : StudentSchema):
    """
    Create a new student record in the database.
    """
    return stud_obj.create_student(std)



@router.put('/students/{id_up}')
def update_student(id_up : int , std_data : StudentSchema):
    """
    Update an existing student record in the database.
    """
    return stud_obj.update_student_data(id_up , std_data)



@router.delete('/students/{id_del}')
def delete_std_data(id_del : int):
    """
    Delete a student record from the database.
    """
    return stud_obj.delete_student(id_del)



