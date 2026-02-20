from pydantic import BaseModel

class student_Sch(BaseModel):
    id : int
    name : str
    fathers_name : str
    age : int
    