import sqlite3
from sqlite3 import Error
import csv

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.sqlite_version}")
       return conn
   except Error as e:
       print(e)

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
       print("Wykonano SQL")
   except Error as e:
       print(e)

def add_clean_measure(conn, measure):
   """
   Create a new measure into the clean_measure table
   :param conn:
   :param measure:
   :return: station
   """
   sql = '''INSERT INTO clean_measure(station, date, precip, tobs)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, measure)
   conn.commit()
   return cur.lastrowid

def add_clean_station(conn, station):
   """
   Create a new station into the clean_stations table
   :param conn:
   :param station:
   :return: station
   """
   sql = '''INSERT INTO clean_stations(station, latitude, longitude, elevation, name, country, state)
             VALUES(?,?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, station)
   conn.commit()
   return cur.lastrowid

def load_stations(conn):
    with open("clean_stations.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            station = (
                row["station"],
                float(row["latitude"]),
                float(row["longitude"]),
                float(row["elevation"]),
                row["name"],
                row["country"],
                row["state"]
            )
            add_clean_station(conn, station)

def load_measures(conn):
    with open("clean_measure.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            measure = (
                row["station"],
                row["date"],
                float(row["precip"]),
                int(row["tobs"])
            )
            add_clean_measure(conn, measure)

if __name__ == "__main__":
    conn = create_connection("weather.db")
    conn.execute("PRAGMA foreign_keys = ON")
    
    sql = """
        -- projects clean_stations
        CREATE TABLE IF NOT EXISTS clean_stations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station TEXT NOT NULL UNIQUE,
        latitude REAL,
        longitude REAL,
        elevation REAL,
        name text NOT NULL,
        country text NOT NULL,
        state text NOT NULL
        );
        """
    execute_sql(conn, sql)

    sql = """
        -- zadanie clean_measure
        CREATE TABLE IF NOT EXISTS clean_measure (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station TEXT NOT NULL,
        date text NOT NULL,
        precip REAL,
        tobs INTEGER,
        FOREIGN KEY (station) REFERENCES clean_stations (station)
        );
        """
    execute_sql(conn, sql)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(clean_stations)")
    print(cursor.fetchall())
    cursor.execute("PRAGMA table_info(clean_measure)")
    print(cursor.fetchall())
    cursor.execute("PRAGMA foreign_key_list(clean_measure)")
    print(cursor.fetchall())
    load_stations(conn)
    load_measures(conn)
    print(conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall())
    

    conn.close()