import os
import psycopg2

def databaseConnectionSetup():
    db_host = os.getenv("DATABASE_HOST", "db") 
    
    conn = psycopg2.connect(
        dbname="bincom_test_db",
        user="admin",
        password="pass",
        host="localhost", # Change "localhost" to "db"
        port="5432"
    )
    return conn