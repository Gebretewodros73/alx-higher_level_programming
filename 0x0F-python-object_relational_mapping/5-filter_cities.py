#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password,
                         db=database, host='localhost', port=3306)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve the states
    query = "SELECT cities.name FROM cities INNER JOIN\
            states ON states.id=cities.state_id\
            WHERE states.name=%s"
    cursor.execute(query, (state, ))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    tmp = list(row[0] for row in rows)
    """ Display the cities as a single line
    separated by commas"""
    print(*tmp, sep=", ")

    # Close the cursor and database connection
    cursor.close()
    db.close()
