#!/usr/bin/python3

"""
Write a script that lists all City objects from the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City).order_by(City.id)

    for row in rows:
        print('{}: {} -> {}'.format(row.id, row.name, row.state.name))
