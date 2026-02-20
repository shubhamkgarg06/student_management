from app.utils.connection_manag import get_connection , release_connection


sql = """
        CREATE TABLE IF NOT EXISTS student (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            fathers_name VARCHAR(255),
            age INT
        )
        """

def create_student_table():

    conn  = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
        print("Student Table Created")
    except Exception as e:
        print("Error creating table:", e)
        conn.rollback()
        raise
    finally:
        cur.close()
        release_connection(conn)
