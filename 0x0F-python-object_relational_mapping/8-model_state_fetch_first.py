#!/usr/bin/python3

"""
Write a script that prints the first State object from the database
hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    # Base.metadata.createall()
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).first()
    print("Nothing" if not rows else "{}: {}".format(rows.id, rows.name))
