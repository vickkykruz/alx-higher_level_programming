#!/usr/bin/python3

"""
write a script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa:
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    rows = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all()

    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
