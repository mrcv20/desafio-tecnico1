from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import DevelopmentConfig

engine = create_engine(
        DevelopmentConfig.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
Session = sessionmaker(autocommit=False, bind=engine)
session = Session()
Base = declarative_base()