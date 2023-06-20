#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
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
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create all tables defined in the Base
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all states with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    if states:
        # Delete the states
        for state in states:
            session.delete(state)
        session.commit()

    # Close the session
    session.close()
