#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)
