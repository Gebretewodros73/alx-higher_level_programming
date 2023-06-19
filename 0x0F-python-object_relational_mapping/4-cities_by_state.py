#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa using SQLAlchemy.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password,
                         db=database, host='localhost', port=3306)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve the states
    query = "SELECT cities.id, cities.name, states.name FROM\
            cities INNER JOIN states ON states.id=cities.state_id"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
