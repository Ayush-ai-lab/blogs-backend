from sqlalchemy import Column, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(255))
    email = Column(String(255)  , unique = True)
    password = Column(String(255))  

    blogs = relationship(
    "Blog",
    back_populates="user"
)