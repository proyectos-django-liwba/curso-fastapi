from pydantic import BaseModel, Field
from typing import Optional

class CategoryTask(BaseModel):
  id: int
  name: str
  description: Optional[str] = Field(None, max_length=100)
 