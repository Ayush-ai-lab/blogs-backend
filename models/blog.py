from sqlalchemy import Column,Integer, String, DateTime,Text 
from core.database import Base 

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    slug = Column(String(255), unique = True)
    short_description = Column(String(255))
    description = Column(Text)
    create_at = Column(DateTime,default=datetime.utcnow)
