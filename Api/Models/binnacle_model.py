from pydantic import BaseModel
from typing import Optional

class Binnacle(BaseModel):
    id: Optional[int] = None
    action: str
    error: str
    status_code: int

    class Config:
        orm_mode = True
        
    def __str__(self):  
        return f"Binnacle(id={self.id}, action={self.action}, error={self.error}, status_code={self.status_code})"