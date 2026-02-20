from fastapi import FastAPI
from routers import student
from models.students import create_student_table


create_student_table()

app = FastAPI()

app.include_router(student.router)
