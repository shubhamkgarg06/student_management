"""
    This module consist of all CRUD mehtod functions for student data.
"""
from app.models.students import StudentModel
from app.schemas.student import StudentSchema , StudentPatchSchema


class StudentCRUD:

    """
    Handles all CRUD operations on student data
    """
    
    def __init__(self, db):
        self.db = db
    

    def get_all_students(self):
        """
        Return all student data present in database
        """
        students = self.db.query(StudentModel).all()
        return students



    def get_student_by_id(self, id_find: int):
        """
        Return a student record from the database using the student's ID.
        """

        student = self.db.query(StudentModel).filter(StudentModel.id == id_find).first()

        if student is None:
            return {"message": "No such student exists"}
        
        return student



    def create_student(self, new_student: StudentSchema):
        """
        Creates a student record in the database..
        """

        # 🔍 Check if student already exists
        existing_student = self.db.get(StudentModel, new_student.id)

        if existing_student:
            return {"message": "Student with this ID already exists"}
        
        # 📦 Create a new student record
        new_student_model = StudentModel(
            id=new_student.id,
            name=new_student.name,
            father_name=new_student.father_name,
            age=new_student.age
        )

        self.db.add(new_student_model)
        self.db.commit()
        self.db.refresh(new_student_model)

        return {"message": "Student created successfully"}



    def update_student_data(self , id_up:int , updated_student: StudentSchema):
        """
        Updates the student record in the database as instructed using student id
        """

        student = self.db.get(StudentModel , id_up)

        if student is None:
            return {"message": "No such student exists"}
        
        student.name = updated_student.name
        student.father_name = updated_student.father_name
        student.age = updated_student.age

        self.db.commit()
        self.db.refresh(student)

        return student



    def delete_student(self, student_id: int):
        """
        Delete a student record from the database using the student's ID.
        """
        student = self.db.get(StudentModel, student_id)

        if student is None:
            return {"message": "No such student exists"}

        self.db.delete(student)
        self.db.commit()

        return student



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

        return student
 
