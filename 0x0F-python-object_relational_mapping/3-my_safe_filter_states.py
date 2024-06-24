#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to database
    user = argv[1]
    passwd = argv[2]
    database_name = argv[3]

    # Establish connection to database
    db_connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=user, passwd=passwd,
        db=database_name, charset="utf8")

    # Create cursor to execute queries
    db_cursor = db_connection.cursor()

    # Execute query
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    db_cursor.execute(query, (argv[4], ))

    # Fetch rows
    query_rows = db_cursor.fetchall()

    # Print rows
    for row in query_rows:
        print(row)

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()
