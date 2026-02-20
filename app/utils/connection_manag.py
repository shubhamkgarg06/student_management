import os
import psycopg2
from config import DATABASE_URL


def get_connection():
    try:
        # Establish connection
        conn = psycopg2.connect(
            DATABASE_URL
        )

        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise