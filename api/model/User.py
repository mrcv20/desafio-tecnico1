from ..database.database import Base
from typing import List
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(20))
    lastName = Column(String(20))
    birthdate = Column(Date, default=datetime.utcnow())
    password = Column(String(60), nullable=True)
    addresses = relationship("Address", primaryjoin="User.id == Address.user_id", cascade='all, delete-orphan')

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(60))
    number = Column(Integer)
    city = Column(String(25))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False) 
    user = relationship("User", back_populates="addresses")   
