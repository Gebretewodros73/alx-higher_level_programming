#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and establish connection to the database
    engine = create_engine(f'mysql+mysqldb://{username}\
            :{password}@localhost:3306/{database}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects and sort them by id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
