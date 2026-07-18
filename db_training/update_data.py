import sqlite3
from conn import create_connection
from execute_sql import execute_sql
ALLOWED_TABLES = {"tasks", "projects"}
def update(conn, table, id, **kwargs):
   if table not in ALLOWED_TABLES:
    raise ValueError(f"Nieznana tabela: {table}")
   """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

if __name__ == "__main__":
   conn = create_connection("database.db")
   update(conn, "tasks", 1, status="started")
   update(conn, "tasks", 1, status="ended")
   conn.close()