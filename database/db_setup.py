import sqlite3
import os

def execute_sql_file(cursor, sql_file_path):
    # Execute SQL statements from a file.
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)