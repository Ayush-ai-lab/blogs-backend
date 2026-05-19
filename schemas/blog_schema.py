from pydantic import BaseModel 
  
class BlogSchema(BaseModel):
    title : str
    slug : str 
    short_description: str
    
