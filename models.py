
from sqlalchemy import Integer,Column,String
from database import Base

class StudentModel(Base):
    __tablename__="student"

    id= Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)