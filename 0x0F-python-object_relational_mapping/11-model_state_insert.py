#!/usr/bin/python3

"""
Write a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa
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

    # add the data
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Query ti display the id
    row = session.query(State).filter(State.name == "Louisiana").first()

    print('{}'.format(row.id))
