import os
from dotenv import load_dotenv
import psycopg2 as pg2

from dataclasses import dataclass

load_dotenv()

@dataclass
class Database:

    connection = pg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    def create_tables(self):
        CREATE_TABLES = """
            CREATE TABLE IF NOT EXISTS entries(
                id SERIAL PRIMARY KEY,
                entry VARCHAR(255),
                published_date DATE NOT NULL DEFAULT CURRENT_DATE
            );
        """

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_TABLES)
        

    def add_entry(self, entry):
        ADD_ENTRY = """
        INSERT INTO entries (entry)
        VALUES (%s);
        """

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(ADD_ENTRY, (entry,))


    def retrieve_entries(self):
        GET_ENTRY = """
            SELECT * FROM entries;
        """

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_ENTRY)
                return cursor.fetchall()