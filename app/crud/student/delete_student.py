from db.database import get_connection
import psycopg2 
from fastapi import HTTPException


def delete_student_data(id_del : int):

    conn = get_connection()
    cur = conn.cursor()

    try:
        
        sql = """
                DELETE FROM student
                WHERE id = %s
                """
        
        cur.execute(sql , (id_del , ))
        deleted_rows = cur.rowcount
        
        conn.commit()

        if deleted_rows == 0:
            raise HTTPException(status_code=404, detail="Student not found")
        

        return {"message": f"Student with ID {id_del} deleted successfully."}

    except psycopg2.Error as e:

        conn.rollback()
        raise e
    
    finally:
        cur.close()
        conn.close()


