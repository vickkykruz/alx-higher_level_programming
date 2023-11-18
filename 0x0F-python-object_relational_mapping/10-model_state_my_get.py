#!/usr/bin/python3

"""
Write a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    # Connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    row = session.query(State).filter(State.name == '{}'.format(
        sys.argv[4])).first()

    print("Not found" if not row else "{}".format(row.id))
