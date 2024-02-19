from pydantic import BaseModel, Field
from typing import Optional

class CategoryTasks(BaseModel):
  id: Optional[int] = None  
  name: str 
  description: Optional[str] = None
  
  class Config:
    from_attributes = True

 