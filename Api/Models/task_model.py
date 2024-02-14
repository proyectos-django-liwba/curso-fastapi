# Dependencias
from pydantic import BaseModel, field_validator
from typing import List, Optional
# Importaciones
from Core.Enums.task_enum import StatusType
from Core.Validations.validator_models import ValidatorModels
#from Api.Models.category_task_model import CategoryTask
#from Api.Models.user_model import User



class Task(BaseModel):
    id: Optional[int]
    title: str
    status : StatusType
    #category: CategoryTask
    #user: User
    # tags: List[str] = [] # Lista de strings
    # tags: List[dict] = [] # Lista de diccionarios
    #tags: set[str] = set()  # Lista de strings únicos, elimina duplicados

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Tarea 1",
                "status": "Pending",
            }
        }
        
    @field_validator("id")
    def id_validator(cls, value):
        ValidatorModels.not_empty(value, "id")
        return value
    
    @field_validator("id")
    def id_number(cls, value):
        ValidatorModels.is_number(value, "id")
        return value
        
    @field_validator("title")
    def task_validator(cls, value):
        ValidatorModels.not_empty(value, "title")
        return value

    @field_validator("title")
    def task_min_length(cls, value):
        ValidatorModels.min_length(value, "title", 5)
        return value

    @field_validator("title")
    def task_max_length(cls, value):
        ValidatorModels.max_length(value, "title", 100)
        return value

    @field_validator("status")
    def status_validator(cls, value):
        ValidatorModels.not_empty(value, "status")
        return value
    
    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"


    # clases anidadas
    """ class Task(BaseModel):
        id: int
        task: str
        status: StatusType
        category: CategoryTask
        user: User
        # tags: List[str] = [] # Lista de strings
        # tags: List[dict] = [] # Lista de diccionarios
        tags: set[str] = set()  # Lista de strings únicos, elimina duplicados """


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