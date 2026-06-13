from conn import create_connection
from execute_sql import execute_sql

conn = create_connection("database.db")
sql = """INSERT INTO projects(id, nazwa, start_date, end_date)
   VALUES (1,
           "Zrób zadania",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00");"""
execute_sql(conn, sql)
conn.close()