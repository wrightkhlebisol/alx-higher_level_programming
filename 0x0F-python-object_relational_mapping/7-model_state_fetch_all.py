#!/usr/bin/python3
""" List all states with sqlalchemy """
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    args = sys.argv

    if (len(args) >= 4):
        user = args[1]
        passwd = args[2]
        host = 'localhost'
        port = 3306
        db = args[3]
        url = f"mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db}"

        engine = create_engine(url)
        session = Session(engine)

        res = session.query(State)

        for r in res:
            print(f'{r.id}: {r.name}')
