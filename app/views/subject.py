from app.models.subjects import SubjectModel
from app.schemas.subjects import SubjectSchema

class SubjectCRUD:
    """
    Handles all CRUD operations on subject data
    This Module contains the SubjectCRUD class which has methods to perform CRUD operations on subject data in the database.
    """

    def __init__(self, db):
        self.db = db

    
    def get_all_subjects(self):
        """
        Return all subject data present in database
        """
        subjects = self.db.query(SubjectModel).all()
        return subjects

    def get_subject_by_id(self, id_find: int):
        """
        Return a subject record from the database using the subject's ID.
        """

        subject = self.db.query(SubjectModel).filter(SubjectModel.subject_id == id_find).first()

        if subject is None:
            return {"message": "No such subject exists"}

        return subject


    def create_subject(self, new_subject: SubjectSchema):
        """
        Creates a subject record in the database..
        """

        # Check if subject already exists
        existing_subject = self.db.get(SubjectModel, new_subject.subject_id)

        if existing_subject:
            return {"message": "Subject with this ID already exists"}

        subject = SubjectModel(**new_subject.model_dum())
        self.db.add(subject)
        self.db.commit()
        self.db.refresh(subject)

        return {"message": "Subject created successfully"}


    def update_subject(self, id_find: int, updated_subject: SubjectSchema):
        """
        Update an existing subject record in the database.
        """

        subject = self.db.query(SubjectModel).filter(SubjectModel.subject_id == id_find).first()

        if subject is None:
            return {"message": "No such subject exists"}

        subject = SubjectModel(**updated_subject.model_dump())
        self.db.commit()
        self.db.refresh(subject)

        return {"message": "Subject updated successfully"}