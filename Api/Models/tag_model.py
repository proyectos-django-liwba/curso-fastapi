# Dependencias
from pydantic import BaseModel
from typing import Optional

class Tag(BaseModel):
    id: Optional[int] = None
    name: str
    
    class Config:
        from_attributes = True
    
    def __str__(self):
        return f"Tag(id={self.id}, name={self.name})"

