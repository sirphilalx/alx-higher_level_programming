#!/usr/bin/python3

""" A script that lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa """

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.contains('a')).order_by(
                             State.id).all()
    for state in states_a:
        print("{}: {}".format(state.id, state.name))
