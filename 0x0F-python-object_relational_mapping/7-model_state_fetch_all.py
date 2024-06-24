#!/usr/bin/python3
"""List all states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

# Connect to db and create tables
if __name__ == "__main__":
    # Connect to db
    user, password, db_name = argv[1:4]
    db_url = ('mysql+mysqldb://{}:{}@localhost/{}'
              .format(user, password, db_name))
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Prepare session
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    # Retrieve states from db
    # /* Loop through all states in db */
    states = session.query(State).order_by(State.id).all()
    for state in states:
        # /* Print state id and name */
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
