from sqlalchemy import Column, Integer, VARCHAR
from database.settings import Base

# This file contains out database table

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    display_name = Column(VARCHAR(256), index=True)
    url = Column(VARCHAR(2083), index=True)