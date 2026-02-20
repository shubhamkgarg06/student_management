import psycopg2
from psycopg2 import pool
from app.config import DATABASE_URL


conn_pool = None

def init_db():

    try:
        global conn_pool

        conn_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=DATABASE_URL
        )

        if conn_pool:
            print("Connection pool created successfully")
    

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise



def get_connection():
    if conn_pool is None:
        raise Exception("Connection pool is not initialized")
    return conn_pool.getconn()


def release_connection(conn):
    conn_pool.putconn(conn)


# def get_connection():

#     try:
#         # Establish connection
#         conn = psycopg2.connect(
#             DATABASE_URL
#         )

#         return conn

#     except psycopg2.Error as e:
#         print(f"Error connecting to the database: {e}")
#         raise