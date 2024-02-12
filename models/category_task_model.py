from pydantic import BaseModel, Field
from typing import Optional

class CategoryTask(BaseModel):
  id: int
  name: str
  description: Optional[str] = Field(None, max_length=100)
  
  class Config:
    from_attributes = True
    json_schema_extra = {
      "example": {
        "name": "Tarea",
        "description": "Descripción de la tarea"
      }
    }
 