"""
    This module consist of all CRUD method functions for section data.
    It includes methods for getting all sections, getting a section by ID, creating a new section,
    and retrieving students by section name.
"""
from app.models.section_model import SectionModel

class SectionCRUD:

    """
    Handles all CRUD operations on data in section table in database.
    """

    def __init__(self, db):
        """
        Initializes the SectionCRUD class with a database session.
        """
        self.db = db



    def get_students_by_section_name(self, section_name: str):
        """
        Return all students in a section given the section name.
        It return a list of student records that belong to the specified section.
        """

        # Find the section by name
        section = self.db.query(SectionModel).filter(SectionModel.section_name == section_name).first()
        if not section:
            return {"message": "Section not found"}

        # Return all students in that section
        return section.students


