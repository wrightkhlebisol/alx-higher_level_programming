#!/usr/bin/python3
""" State class - instance of Base """
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine("mysql+mysqldb://root:root@localhost/db_name/")
Base = declarative_base()


class State(Base):
    """ State class with class attributes """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement)
    name = Column(String(128), nullable=False)
