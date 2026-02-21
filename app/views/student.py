"""
    This module consist of all CRUD mehtod functions for student data.
"""

from app.utils.connection_manag import sessionLocal
from app.models.students import Student_mod
from app.schemas.student import student_Sch


class StudentCRUD:

    """
    Handles all CRUD operations on student data
    """

    def __init__(self):
        self.db = sessionLocal()



    def get_all_students(self):
        """
        Return all student data present in database
        """
        students = self.db.query(Student_mod).all()
        return students



    def get_student_by_id(self, student_id: int):
        """
        Return a student record from the database using the student's ID.
        """

        student = self.db.query(Student_mod).filter(Student_mod.id == student_id).first()

        if student is None:
            return {"mesage" : "No such student exist"}
        return student



    def create_student(self, student: student_Sch):
        """
        Creates a student record in the database..
        """

        new_student = Student_mod(
            id=student.id,
            name=student.name,
            fathers_name=student.fathers_name,
            age=student.age
        )

        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)

        return {"message": "Student created successfully"}



    def update_student_data(self , student_id:int , updated_student: student_Sch):
        """
        Updates the student record in the database as instructed using student id
        """

        student = self.db.get(Student_mod , student_id)

        if student is None:
            return None
        
        student.name = updated_student.name
        student.fathers_name = updated_student.fathers_name
        student.age = updated_student.age

        self.db.commit()
        self.db.refresh(student)

        return student



    def delete_student(self, student_id: int):
        """
        Delete a student record from the database using the student's ID.
        """
        student = self.db.get(Student_mod, student_id)

        if student is None:
            return None

        self.db.delete(student)
        self.db.commit()

        return student


