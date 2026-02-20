from db.database import get_connection
import psycopg2 
from schemas.student import student_Sch


def post_new_students(std : student_Sch ):

    conn = get_connection()    

    try:
        cur = conn.cursor()
        sql = """
                INSERT into student (id , name , fathers_name , age)
                values (%s , %s , %s , %s)
            """

        cur.execute(sql , (std.id , std.name , std.fathers_name , std.age ,))

        conn.commit()
        cur.close()
        

        
        return  {"message": f"Student {std.id} inserted successfully"}
    

    except psycopg2.Error as e:

        conn.rollback() 
        raise e
    

    finally:
        conn.close()