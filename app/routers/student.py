from fastapi import APIRouter
from views.student import StudentCRUD
from schemas.student import student_Sch




router = APIRouter()
stud_obj = StudentCRUD()


@router.get('/students/')
def get_students():
    return stud_obj.get_all_students()

@router.get('/students/{id_find}')
def get_std_id(id_find : int):
    return stud_obj.get_student_by_id(id_find)


@router.post('/students/')
def add_student(std : student_Sch):
    return stud_obj.create_student(std)



@router.put('/students/{id_up}')
def update_student(id_up : int , std_data : student_Sch):
    return stud_obj.update_student_data(id_up , std_data)



@router.delete('/students/{id_del}')
def delete_std_data(id_del : int):
    return stud_obj.delete_student(id_del)



