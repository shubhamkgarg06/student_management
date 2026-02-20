from fastapi import APIRouter
from crud.student.get_student import get_all_students, get_student_by_id
from crud.student.post_student import post_new_students
from schemas.student import student_Sch
from crud.student.put_student import update_student_data
from crud.student.delete_student import delete_student_data





router = APIRouter()


@router.get('/students/')
def get_students():
    return get_all_students()

@router.get('/students/{id_find}')
def get_std_id(id_find : int):
    return get_student_by_id(id_find)


@router.post('/students/')
def add_student(std : student_Sch):
    return post_new_students(std)



@router.put('/students/{id_up}')
def update_student(id_up : int , std_data : student_Sch):
    return update_student_data(id_up , std_data)



@router.delete('/students/{id_del}')
def delete_std_data(id_del : int):
    return delete_student_data(id_del)



