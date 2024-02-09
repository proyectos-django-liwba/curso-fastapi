from pydantic import BaseModel,field_validator
from assets.enums.task_enum import StatusType
from assets.validators.validator_models import ValidatorModels
from models.category_task_model import CategoryTask
from models.user_model import User
from typing import List

class Task(BaseModel):
    id: int
    task: str 
    status: StatusType
    category: CategoryTask
    user: User
    #tags: List[str] = [] # Lista de strings
    #tags: List[dict] = [] # Lista de diccionarios
    tags:  set[str] = set() # Lista de strings únicos, elimina duplicados
    

    @field_validator("task")
    def task_validator(cls, value):
      ValidatorModels.not_empty(value, "task")
      return value
    
    @field_validator("task")
    def task_min_length(cls, value):
      ValidatorModels.min_length(value, "task", 5)
      return value
    
    @field_validator("task")
    def task_max_length(cls, value):
      ValidatorModels.max_length(value, "task", 100)
      return value
    
    @field_validator("status")
    def status_validator(cls, value):
      ValidatorModels.not_empty(value, "status")
      return value
 
