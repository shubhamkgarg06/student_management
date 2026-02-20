from fastapi import FastAPI
from routers import student
from app.utils.connection_manag import init_db
from models.students import create_student_table

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()
    create_student_table()



app.include_router(student.router)
