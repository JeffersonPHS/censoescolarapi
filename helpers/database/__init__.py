import os
import psycopg2
from flask import g
from dotenv import load_dotenv
from helpers.application import app

load_dotenv()


#DATABASE = 'censoescolar.db'


def get_connection():
    conn = getattr(g, '_database', None)
    if conn is None:
      conn = g._database = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
    return conn


@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()





