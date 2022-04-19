from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime
from database import Base
import datetime


class User_address(Base):
    __tablename__ = 'user_address'

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    address2 = Column(String)
    district = Column(String)
    Latitude = Column(Integer)
    Longitude = Column(Float)
    postal_code = Column(Float)
    phone = Column(Integer)
    city = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.now,onupdate=datetime.datetime.now)

