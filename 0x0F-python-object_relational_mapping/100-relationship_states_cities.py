#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
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

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
