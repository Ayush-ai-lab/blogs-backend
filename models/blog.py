from sqlalchemy import Column, ForeignKey,Integer, String, DateTime,Text 
from core.database import Base 
from sqlalchemy.orm import relationship
from datetime import datetime
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    slug = Column(String(255), unique = True)
    short_description = Column(String(255))
    description = Column(Text)
    create_at = Column(DateTime,default=datetime.utcnow)
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="blogs"
    )
