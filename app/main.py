"""
Main entry point of the Student Management API application.

This module initializes the FastAPI app instance,
registers API routers, and creates database tables on startup.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import student
from app.utils.connection_manag import engine,Base



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
app = FastAPI()


# Include the student router to handle student-related API endpoints.
app.include_router(student.router)
