#!/usr/bin/python3

""" A script that adds the State object “Louisiana” to
    the database hbtn_0e_6_usa """

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    new_state_id = session.query(State).filter(State.name ==
                                               "Louisiana").first()
    try:
        print(new_state_id.id)
    except Exception:
        print("Not found")
