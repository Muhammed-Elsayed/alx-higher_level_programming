#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    sessions_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()
    for to_delete_sess in sessions_to_delete:
        session.delete(to_delete_sess)

    session.commit()
