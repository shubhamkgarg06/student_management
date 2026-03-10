"""
Main entry point of the Student Management API application.

This module initializes the FastAPI app instance,
registers API routers, and creates database tables on startup.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import mid_term_marks, student , section, subject
from app.utils.connection_manag import DatabaseManager

Base = DatabaseManager.Base
engine = DatabaseManager.engine

@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Manage application startup and shutdown events.

    Creates database tables at startup.
    """
    # Startup logic
    Base.metadata.create_all(bind=engine)
    yield



# Create a FastAPI application instance.
app = FastAPI(lifespan=lifespan)

@app.get('/')
def home():
    """
    Home endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Student API!"}


# Include the student router to handle student-related API endpoints.
app.include_router(student.router)
app.include_router(section.router)
app.include_router(subject.router)
app.include_router(mid_term_marks.router)
