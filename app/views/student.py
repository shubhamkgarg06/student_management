"""
    This module consist of all CRUD mehtod functions for student data.
"""
from app.models.student_model import StudentModel
from app.schemas.student_schema import StudentSchema , StudentPatchSchema


class StudentCRUD:

    """
    Handles all CRUD operations on student data
    """

    def __init__(self, db):
        self.db = db


    def get_student_by_section_id(self, section_id_find: int):
        """
        Return all students in a specific section.
        """

        students = self.db.query(StudentModel).filter(StudentModel.section_id == section_id_find).all()

        if not students:
            return {"message": "No students found in this section"}

        return students



    def create_student(self, new_student: StudentSchema):
        """
        Creates a student record in the database..
        """

        # Check if student already exists
        existing_student = self.db.get(StudentModel, (new_student.id , new_student.section_id))

        if existing_student:
            return {"message": "Student with this ID already exists"}

        # Create a new student record
        new_student_model = StudentModel(**new_student.model_dump())

        self.db.add(new_student_model)
        self.db.commit()
        self.db.refresh(new_student_model)

        return {"message": "Student created successfully"}



    def update_student(self, student_id: int, section_id: int, updated_data: StudentSchema):
        """
        Updates the student record in the database.
        """

        student = self.db.get(StudentModel, (student_id , section_id))

        if student is None:
            return {"message": "No such student exist"}

        for key, value in updated_data.model_dump().items():
            setattr(student, key, value)

        self.db.commit()
        self.db.refresh(student)

        return {"message": "Student data updated successfully"}
    
    def delete_student_record(self, student_id: int, section_id: int):
        """
        Deletes the student record from the database.
        """

        student = self.db.get(StudentModel, (student_id , section_id))

        if student is None:
            return {"message": "No such student exist"}

        self.db.delete(student)
        self.db.commit()

        return {"message": "Student record deleted successfully"}
    
    
    def patch_student_data(self, student_id : int , updated_data: StudentPatchSchema):
        """
        Partially updates the student fields
        """

        student = self.db.get(StudentModel , student_id)

        if student is None:
            return {"message" : "No such student exist"}
   
        update_data = updated_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(student, key, value)

        self.db.commit()
        self.db.refresh(student)

        return {"message" : "Student data patched successfully"}
 
