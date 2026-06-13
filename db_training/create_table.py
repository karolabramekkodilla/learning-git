from conn import create_connection
from execute_sql import execute_sql

conn = create_connection("database.db")
sql = """
-- zadanie table
CREATE TABLE IF NOT EXISTS tasks (
  id integer PRIMARY KEY,
  project_id integer NOT NULL,
  nazwa VARCHAR(250) NOT NULL,
  opis TEXT,
  status VARCHAR(15) NOT NULL,
  start_date text NOT NULL,
  end_date text NOT NULL,
  FOREIGN KEY (project_id) REFERENCES projects (id)
);
"""
execute_sql(conn, sql)
sql = """
-- projects table
CREATE TABLE IF NOT EXISTS projects (
  id integer PRIMARY KEY,
  nazwa text NOT NULL,
  start_date text,
  end_date text
);
"""

execute_sql(conn, sql)
conn.close()
