from fastapi import FastAPI
from routers import student
from utils.connection_manag import engine,Base

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)



app.include_router(student.router)
