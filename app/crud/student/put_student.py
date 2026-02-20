from db.database import get_connection
import psycopg2 
from schemas.student import student_Sch
from fastapi import HTTPException



def update_student_data(id_up : int , stud_data : student_Sch):

    conn = get_connection()
    cur = conn.cursor()

    try:
        
        sql = """
                UPDATE student
                SET name = %s, 
                    fathers_name = %s , 
                    age = %s 
                WHERE id = %s;
            """
        
        cur.execute(sql , (stud_data.name  , stud_data.fathers_name , stud_data.age , id_up, ))

        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        conn.commit()
        return {"message": f"Student with ID {id_up} updated successfully."}
       
        
        
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    
    finally:
        cur.close()
        conn.close()
       