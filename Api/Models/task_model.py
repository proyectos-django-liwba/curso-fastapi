# Dependencias
from pydantic import BaseModel
from typing import List, Optional
# Importaciones
from Core.Enums.task_enum import StatusType

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    status : StatusType
    category_task_id: int
    user_id: int
    
    class Config:
        from_attributes = True
     
    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"
            
