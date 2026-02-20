"""
    This module consist of all CRUD mehtod functions for student data.
"""

from utils.connection_manag import sessionLocal
from schemas.student import student_Sch
from models.students import Student_mod

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



    # def get_student_by_id(self, student_id: int):
    #     """
    #     Return a student record from the database using the student's ID.
    #     """
    #     sql = "SELECT * FROM student WHERE id = %s"
    #     self.cur.execute(sql, (student_id,))
    #     return self.cur.fetchone()



    # def create_student(self, student: student_Sch):
    #     """
    #     Creates a student record in the database..
    #     """

    #     sql = """
    #         INSERT INTO student (id, name, fathers_name, age)
    #         VALUES (%s, %s, %s, %s)
    #     """
    #     self.cur.execute(sql, (student.id, student.name, student.fathers_name, student.age))
    #     self.conn.commit()
    #     return {"message": "Student created successfully"}



    # def update_student_data(self , student_id:int , student: student_Sch):
    #     """
    #     Updates the student record in the database as instructed using student id
    #     """

    #     sql = """
    #                 UPDATE student
    #                 SET name = %s , fathers_name = %s , age = %s
    #                 WHERE id = %s
    #         """  
         
    #     self.cur.execute(sql , (student.name , student.fathers_name , student.age , student_id ,))
    #     self.conn.commit()
    #     return {"message": "Student data updated"}
    


    # def delete_student(self, student_id: int):
    #     """
    #     Delete a student record from the database using the student's ID.
    #     """
    #     sql = "DELETE FROM student WHERE id = %s"
    #     self.cur.execute(sql, (student_id,))
    #     self.conn.commit()
    #     return {"message": "Deleted successfully"}  


