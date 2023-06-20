#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Create all tables defined in the Base
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit the changes
    session.add(new_state)
    session.commit()

    # Display the new state's id
    print(new_state.id)

    # Close the session
    session.close()
