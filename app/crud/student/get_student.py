from db.database import get_connection
import psycopg2 


def get_all_students():

    conn = get_connection()    

    try:
        cur = conn.cursor()
        sql = "SELECT * FROM student"

        cur.execute(sql)

        student_data = cur.fetchall()

        columns = [desc[0] for desc in cur.description]

        student_list = []
        for row in student_data:
            product = dict(zip(columns, row))
            student_list.append(product)
        
        conn.commit()
        cur.close()
        return student_list
    

    except psycopg2.Error as e:

        return {"error": f"Database error during retrieval: {e}"}
    

    finally:
        conn.close()





def get_student_by_id(id_find : int):

    conn = get_connection()    

    try:
        cur = conn.cursor()
        sql = "SELECT * FROM student where id = %s"
 
        cur.execute(sql , (id_find , ))

        student_data = cur.fetchone()

        

        if student_data:

            cols = [desc[0] for desc in cur.description]
            student = dict(zip(cols, student_data))
            return student
        
        return {"message": f"Student with ID {id_find} not found."}
    

    except psycopg2.Error as e:

        raise e
    

    finally:
        cur.close()
        conn.close()
