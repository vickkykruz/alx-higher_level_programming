#!/usr/bin/python3

"""
Write a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id)

    for row in rows:
        print('{}: {}'.format(row.id, row.name))
        for city in row.cities:
            print(' {}: {}'.format(city.id, city.name))
