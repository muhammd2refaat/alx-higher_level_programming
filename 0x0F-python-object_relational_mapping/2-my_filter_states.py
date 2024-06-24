#!/usr/bin/python3
"""Lists states by name with personal assistance"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to database
    database_host = "localhost"
    database_port = 3306
    database_user = argv[1]
    database_passwd = argv[2]
    database_name = argv[3]
    database_charset = "utf8"

    database_connection = MySQLdb.connect(
        host=database_host, port=database_port,
        user=database_user, passwd=database_passwd,
        db=database_name, charset=database_charset)

    # Create cursor to execute query
    database_cursor = database_connection.cursor()

    # Formulate query
    query_template = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query_template.format(argv[4])

    # Execute query
    database_cursor.execute(query)

    # Fetch rows
    query_rows = database_cursor.fetchall()

    # Print rows
    for row in query_rows:
        print(row)

    # Close cursor and connection
    database_cursor.close()
    database_connection.close()
