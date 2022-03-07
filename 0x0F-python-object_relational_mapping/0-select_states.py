#!/usr/bin/python3
""" Select all state from database and diplay it."""
from sqlalchemy import create_engine, Table, Integer, String, Column, select
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import pymysql

Base = declarative_base()

username = sys.argv[1]
password = sys.argv[2]
dbName = sys.argv[3]
host = 'localhost'
port = 3306


class states(Base):
    """states model definition or their schema"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<states %r>" % self.username


if __name__ == "__main__":

    db_url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
             username, password, host, port, dbName)
    # create database engine / connect to the database
    db_engine = create_engine(db_url)

    connection = db_engine.connect()
    connection = connection.execution_options(
        isolation_level="READ COMMITTED"
    )

    s = select([states])
    result = connection.execute(s)

    for row in result:
        print(row)
