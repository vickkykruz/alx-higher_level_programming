#!/usr/bin/python3

"""
Write a script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
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

    # Delete Query
    rows = session.query(State).filter(State.name.like('%a%')).all()

    for row in rows:
        session.delete(row)

    session.commit()
