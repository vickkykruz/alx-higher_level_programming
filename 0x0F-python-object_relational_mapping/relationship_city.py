#!/usr/bin/python3

"""
Write a Python file similar to model_state.py named model_city.py that
contains the class definition of a City.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ This is a class city that inherit both the Base and State """
    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False)

    name = Column(
            String(128),
            nullable=False)

    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
