from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import DevelopmentConfig, TestingConfig
from os import getenv


engine = create_engine(
        DevelopmentConfig.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
if getenv('FLASK_ENV') in ['testing']:
        engine = create_engine(
        TestingConfig.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)


Session = sessionmaker(autocommit=False, bind=engine)
session = Session()
Base = declarative_base()