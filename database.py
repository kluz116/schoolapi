from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password = 'Musembya*26'

#Database_Connection_String = "postgresql://odoo12:@localhost/schoolapi"
#Database_Connection_String="postgresql:///schoolapi"
Database_Connection_String ="mysql+pymysql://root:{}@localhost:3306/schoolapi".format(password)
engine = create_engine(Database_Connection_String)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()