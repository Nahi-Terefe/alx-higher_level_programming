#!/usr/bin/python3
from sqlalchemy import create_engine, Table, Integer, String, Column
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
    """states account."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<states %r>" % self.username


db_url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
         username, password, host, port, dbName)
# create database engine / connect to the database
db_engine = create_engine(db_url)


# let's create a session
# Session = sessionmaker(bind=db_engine)
# session = Session()

# for state in session.query(states):
#     print(state.name)


# # query for existing database
# existing_db = db_engine.execute("SHOW DATABASES;")
# existing_db = [d[0] for d in existing_db]

connection = db_engine.connect()
connection = connection.execution_options(
    isolation_level="READ COMMITTED"
)

s = select([states])
result = connection.execute(s)

for row in result:
    print(row)

# print("existing databases are: ")
# print(existing_db)
