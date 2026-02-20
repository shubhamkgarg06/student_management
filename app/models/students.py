from sqlalchemy import Column, Integer, String
from app.utils.connection_manag import Base
from app.utils.connection_manag import engine, Base


class Student_mod(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fathers_name = Column(String)
    age = Column(Integer)


# sql = """
#         CREATE TABLE IF NOT EXISTS student (
#             id INT PRIMARY KEY,
#             name VARCHAR(255),
#             fathers_name VARCHAR(255),
#             age INT
#         )
#         """

# def create_student_table():

#     conn  = get_connection()
#     cur = conn.cursor()

#     try:
#         cur.execute(sql)
#         conn.commit()
#         print("Student Table Created")
#     except Exception as e:
#         print("Error creating table:", e)
#         conn.rollback()
#         raise
#     finally:
#         cur.close()
#         release_connection(conn)
