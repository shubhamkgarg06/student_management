from db.database import get_connection


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
        conn.close()


if __name__ == "__main__":
    create_student_table()
