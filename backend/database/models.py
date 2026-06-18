from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    country = Column(String(100))


class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    name = Column(String(150))
    category = Column(String(50))
    rating = Column(Float)
    entry_fee = Column(Float)


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    name = Column(String(150))
    budget_type = Column(String(20))
    rating = Column(Float)
    price_per_night = Column(Float)