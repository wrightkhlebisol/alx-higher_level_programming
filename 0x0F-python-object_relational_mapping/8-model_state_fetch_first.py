#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State


if __name__ == '__main__':
    args = sys.argv

    if len(args) >= 4:
        user = args[1]
        passwd = args[2]
        db = args[3]
        url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'

        engine = create_engine(url)
        session = Session(engine)

        res = session.query(State).first()
        print(f'{res.id}: {res.name}')
