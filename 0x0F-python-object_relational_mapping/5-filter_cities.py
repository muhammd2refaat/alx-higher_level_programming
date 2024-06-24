#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to database
    db_connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8")

    # Create cursor to execute query
    cursor = db_connection.cursor()

    # Formulate query
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

    # Execute query with passed argument
    cursor.execute(query, (argv[4], ))

    # Fetch cities names
    cities_names = map(lambda x: x[0], cursor.fetchall())

    # Print cities names
    print(", ".join(cities_names))

    # Close cursor and connection
    cursor.close()
    db_connection.close()
