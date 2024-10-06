from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel  

URL_DB = "mysql+mysqlconnector://root:1123038259@127.0.0.1:3306/consultorio"
crear = create_engine(URL_DB)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=crear)
base = declarative_base()

def get_db():
    cnn = Sessionlocal()
    try:
        yield cnn
    finally:
        cnn.close()