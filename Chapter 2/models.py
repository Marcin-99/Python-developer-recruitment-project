from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Model = declarative_base()


class Task(Model):
    __tablename__ = "task"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    deadline = Column('deadline', DateTime)
    description = Column('description', String)
    hash = Column('hash', String, unique=True)


engine = create_engine('sqlite:///database', echo=False)
Model.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)