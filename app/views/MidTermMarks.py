"""
This module defines the MidTermMarksCRUD class, which handles all CRUD operations for the midterm
marks data in the database. It includes methods for creating new midterm marks records, retrieving all midterm marks, and searching for midterm marks based on specific criteria such as student ID, subject ID, or section ID. The class interacts with the database using SQLAlchemy and uses Pydantic schemas for data validation and serialization.
"""
from app.models.MidTermMarks import MidTermMarksModel
from app.schemas.MidTermMarks import MidTermMarksSchema


class MidTermMarksCRUD:

    """
    Handles all CRUD operations on data in midterm marks table in database.
    """

    def __init__(self, db):
        """
        Initializes the MidTermMarksCRUD class with a database session.
        """
        self.db = db

    
    def create_midterm_marks(self , marks : MidTermMarksSchema):

        """
        This add data to midterm marks table
        """

        existing_marks = self.db.get(
            'MidTermMarksModel' ,
            (marks.student_id , marks.subject_id , marks.section_id)
            )
        
        if existing_marks:
            return {"message": "Marks for this student, subject and section already exist"}

        new_marks_model = MidTermMarksModel(**marks.model_dump())

        self.db.add(new_marks_model)
        self.db.commit()
        self.db.refresh(new_marks_model)

        return {"message": "Marks added successfully"}


    def get_marks_table_data(self ):

        """
        Fetches the marks table data for a specific student.
        """
        marks_data = self.db.query(MidTermMarksModel).all()

        return marks_data


    def get_marks_by_specific_criteria(self , student_id = None , subject_id = None , section_id = None):

        """
        Fetches the marks for a specific student by their ID.
            The method allows filtering the marks based on student ID, subject ID, and section ID. 
            If any of these parameters are provided, the query will be filtered accordingly. 
            If no marks are found for the given criteria, a message indicating that no marks were found will be returned.
            Otherwise, the method will return the list of marks that match the specified criteria.
        """
        query = self.db.query(MidTermMarksModel)

        if student_id is not None:
            query = query.filter(MidTermMarksModel.student_id == student_id)

        if subject_id is not None:
            query = query.filter(MidTermMarksModel.subject_id == subject_id)

        if section_id is not None:
            query = query.filter(MidTermMarksModel.section_id == section_id)

        marks_data = query.all()

        if not marks_data:
            return {"message": "No marks found for the given criteria"}

        return marks_data

