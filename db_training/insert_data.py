from conn import create_connection
from execute_sql import execute_sql
def add_project(conn, project):
   """
   Create a new project into the projects table
   :param conn:
   :param project:
   :return: project id
   """
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   return cur.lastrowid

def add_task(conn, task):
   
   sql = '''INSERT INTO tasks(project_id, nazwa, opis , status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   return cur.lastrowid
   
conn = create_connection("database.db")
# Przykład 1
# sql = """INSERT INTO projects(id, nazwa, start_date, end_date)
#    VALUES (1,
#            "Zrób zadania",
#            "2020-05-08 00:00:00",
#            "2020-05-10 00:00:00");"""
# Przykład 2
# sql = """INSERT INTO projects(nazwa, start_date, end_date)
#    VALUES ( "Zrób zadania 2",
#            "2020-05-08 00:00:00",
#            "2020-05-10 00:00:00");"""
# execute_sql(conn, sql)
# Przykład 3
# project = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
# pr_id = add_project(conn, project)
# print(pr_id)
# Przykład 4
task = ("1","Nauka słówek", "Nauka języka angielskiego czasowniki", "Rozpoczęte", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
tsk_id = add_task(conn, task)
conn.commit()
conn.close()