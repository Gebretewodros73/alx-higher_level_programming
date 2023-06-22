#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    Class definition of a City.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
