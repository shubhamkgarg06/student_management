"""
This module defines a BaseCRUD class that provides basic CRUD (Create, Read, Update, Delete) operations for a given SQLAlchemy model. The class is designed to be reusable and can be used as a base class for specific models to avoid code duplication. It includes methods for retrieving all records, retrieving a record by ID, creating a new record, updating an existing record, and deleting a record.
"""

class BaseCRUD:

    """
        This class provides basic CRUD operations for a given SQLAlchemy model.
          It can be used as a base class for specific models to avoid code duplication and promote reusability. The class includes methods for retrieving all records, retrieving a record by ID, creating a new record, updating an existing record, and deleting a record.
    """

    def __init__(self , db, model):
        """
        Initializes the BaseCRUD instance with a database session and a SQLAlchemy model.
        :param db: The database session to be used for CRUD operations.
        :param model: The SQLAlchemy model class that this CRUD class will operate on.
        """

        self.db = db
        self.model = model
    

    def get_all_records(self):
        """
        Retrieves all records of the specified model from the database.
        :return: A list of all records of the specified model.
        """

        data = self.db.query(self.model).all()
        return data
    

    def get_record_by_id(self , id_find):
        """
        Retrieves a single record of the specified model from the database using its ID.
        :param id_find: The ID of the record to be retrieved.
        :return: The record with the specified ID, or a message if no such record exists"""

        data = self.db.query(self.model).filter(self.model.id == id_find).first()

        if data is None:
            return {"message": "No such data exists"}
        return data
    


    def create_record(self , schema):

        """
        Creates a new record in the database using the provided schema.
        :param schema: The Pydantic schema containing the data for the new record.
        :return: A message indicating the success of the operation, or a message if a record with the same ID already exists."""

        existing_record = self.db.get(self.model, schema.id)

        if existing_record:
            return {"message": "Record with this ID already exists"}
        

        new_student_model = self.model(**schema.model_dump())

        self.db.add(new_student_model)
        self.db.commit()
        self.db.refresh(new_student_model)

        return {"message": "Data Added successfully"}
    



    def update_record(self , id_up , updated_schema):

        """
        Updates an existing record in the database using the provided ID and schema.
        :param id_up: The ID of the record to be updated.
        :param updated_schema: The Pydantic schema containing the updated data.
        :return: A message indicating the success of the operation, or a message if no such record exists.
        """

        data = self.db.get(self.model , id_up)

        if data is None:
            return {"message": "No such data exists"}

        update_data = updated_schema.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(data, key, value)

        self.db.commit()
        self.db.refresh(data)

        return {"message": "Data updated successfully"}
    


    def delete_record(self , id_del):

        """
        Deletes a record from the database using the provided ID.
        :param id_del: The ID of the record to be deleted.
        :return: A message indicating the success of the operation, or a message if no such record exists.
        """

        data = self.db.get(self.model, id_del)

        if data is None:
            return {"message": "No such data exists"}

        self.db.delete(data)
        self.db.commit()

        return {"message" : "Data deleted successfully"}

