"""
    This module consist of all CRUD method functions for section data.
"""
from app.models.section import SectionModel
from app.schemas.section import SectionSchema

class SectionCRUD:

    """
    Handles all CRUD operations on section data
    """

    def __init__(self, db):
        self.db = db


    def get_all_sections(self):
        """
        Return all section data present in database
        """
        sections = self.db.query(SectionModel).all()
        return sections


    def get_section_by_id(self, id_find: int):
        """
        Return a section record from the database using the section's ID.
        """

        section = self.db.query(SectionModel).filter(SectionModel.id == id_find).first()

        if section is None:
            return {"message": "No such section exists"}
        
        return section


    def create_section(self, new_section: SectionSchema):
        """
        Creates a section record in the database..
        """

        # 🔍 Check if section already exists
        existing_section = self.db.get(SectionModel, new_section.id)

        if existing_section:
            return {"message": "Section with this ID already exists"}
        
        # Create a new section record
        new_section_model = SectionModel(
            id=new_section.id,
            section_name=new_section.name
        )

        self.db.add(new_section_model)
        self.db.commit()
        self.db.refresh(new_section_model)



    def get_students_by_section_name(self, section_name: str):
        """
        Return all students in a section given the section name.
        """
        
        # Find the section by name
        section = self.db.query(SectionModel).filter(SectionModel.section_name == section_name).first()
        if not section:
            return {"message": "Section not found"}

        # Return all students in that section
        return section.students
    
