from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///students.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
Base.metadata.create_all(engine)

session = Session(engine)
### Interact with session for database operations