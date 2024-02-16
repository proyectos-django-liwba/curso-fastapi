# Dependencias
from pydantic import BaseModel
from typing import List, Optional
# Importaciones
from Core.Enums.task_enum import StatusType
from Api.Models.category_tasks_model import CategoryTasks
#from Api.Models.user_model import User

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    status : StatusType
    category_task_id: int
    user_id: int
    #user: Optional[User] = None
    
    class Config:
        from_attributes = True
     
    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"
            
   
    # Ejemplo de estructura del modelo
    """ model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "task": "Tarea 1",
                "status": "Pending",
                "category": {"id": 1, "name": "Categoria 1"},
                "user": {"id": 1, "name": "Usuario 1", "email": "correo@correo.com"},
                "tags": ["tag1", "tag2"],
            }
        }
    } """