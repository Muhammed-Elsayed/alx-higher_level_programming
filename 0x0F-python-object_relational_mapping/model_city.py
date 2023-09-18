#!/usr/bin/python3
"""
City class for sqlalchemy
"""

from sqlalchemy import create_engine, Column, Integer, String,\
      Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class City(Base):
    """
    The City class (super class for other classes)
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
