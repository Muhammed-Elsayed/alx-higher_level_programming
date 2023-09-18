#!/usr/bin/python3
"""
sql query for city and state
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    si_city = session.query(State, City).\
        filter(City.state_id == State.id).all()

    for state, city in si_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
