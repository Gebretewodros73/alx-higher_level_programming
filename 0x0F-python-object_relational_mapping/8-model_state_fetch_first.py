#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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
    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first State object from the database
    state = session.query(State).order_by(State.id).first()

    # Display the result
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
