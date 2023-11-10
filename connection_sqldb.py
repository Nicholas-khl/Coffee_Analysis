import os
import psycopg2
from config import db_config

def db_connection():
    db_user = db_config["user"]
    db_password = os.environ.get("DB_PASSWORD")
    db_host = db_config["host"]
    db_port = db_config["port"]
    db_database = db_config["database"]

    try:
        conn = psycopg2.connect(
             user=db_user,
             password=db_password,
             host=db_host,
             port=db_port,
             database=db_database
        )
        return conn
    except psycopg2.Error as error:
           print(f"Error connecting to the PostgreSQL database: {error}")
           return None