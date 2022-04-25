from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password@postgres')
base = declarative_base()

class Mentors(base):
    __tablename__ = 'mentors'
    mentor_id = Column(String, primary_key=True)
    name = Column(String)
    profession = Column(String)
    age = Column(int)
    availability = Column(String)
    status = Column(String)
    date_added = Column(String)

base.metadata.reflect(engine)

Session = sessionmaker(engine)
session = Session()
