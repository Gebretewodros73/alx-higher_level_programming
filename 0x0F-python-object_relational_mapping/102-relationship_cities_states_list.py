#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for ins in session.query(State).order_by(State.id):
        for city in ins.cities:
            print(f"{city.id}: {city.name} -> {ins.name}")

    session.close()
