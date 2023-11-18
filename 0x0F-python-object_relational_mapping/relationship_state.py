#!/usr/bin/python3

"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ This is a class that hold the structure of state """

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)
    name = Column(
            String(128),
            nullable=False)

    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")
