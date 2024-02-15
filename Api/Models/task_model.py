# Dependencias
from pydantic import BaseModel, field_validator
from typing import List, Optional
# Importaciones
from Core.Enums.task_enum import StatusType
from Core.Validations.validator_models import ValidatorModels
#from Api.Models.category_task_model import CategoryTask
#from Api.Models.user_model import User



class Task(BaseModel):
    id: Optional[int] = None
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
        
    def validate_create(self):
        #validar id
        """ ValidatorModels.not_null(self.id, "id")
        ValidatorModels.is_positive_integer(self.id, "id") """
        ValidatorModels.is_number(self.id, "id")
        # validaciones de title
        ValidatorModels.not_empty(self.title, "title")
        ValidatorModels.min_length(self.title, "title", 4)
        ValidatorModels.max_length(self.title, "title", 100)
        # validaciones de status
        ValidatorModels.not_empty(self.status, "status")
        ValidatorModels.min_length(self.status, "status", 4)
        ValidatorModels.max_length(self.status, "status", 20)
        
    def validate_update(self):
        # validaciones de id
        ValidatorModels.not_null(self.id, "id")
        ValidatorModels.is_positive_integer(self.id, "id")
        # validaciones de title
        ValidatorModels.not_empty(self.title, "title")
        ValidatorModels.min_length(self.title, "title", 4)
        ValidatorModels.max_length(self.title, "title", 100)
        # validaciones de status
        ValidatorModels.not_empty(self.status, "status")
        ValidatorModels.min_length(self.status, "status", 4)
        ValidatorModels.max_length(self.status, "status", 20)
        
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