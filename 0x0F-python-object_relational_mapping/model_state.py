#!/usr/bin/python3
"""
Base class for sqlalchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    The state class (super class for other classes)
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)
