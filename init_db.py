import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = None

try:
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

    with open('schema.sql', 'r', encoding='utf-8') as file:
      
        cursor = connection.cursor()
        cursor.execute(file.read())

    connection.commit()

except psycopg2.Error as e:
    print(f'O PostgreSQL lançou uma exceção: {str(e)}')

finally:
    if connection is not None:
        connection.close()