from Api.Models.task_model import Task
from Core.Validations.validator_models import ValidatorModels

class TaskValidation:
    
    def validate_create(task: Task):
        # validaciones de title
        ValidatorModels.not_empty(task.title, "title")
        ValidatorModels.min_length(task.title, "title", 4)
        ValidatorModels.max_length(task.title, "title", 100)
        # validaciones de status
        ValidatorModels.not_empty(task.status, "status")
        ValidatorModels.min_length(task.status, "status", 4)
        ValidatorModels.max_length(task.status, "status", 20)
        
    def validate_update(task):
        # validaciones de id
        ValidatorModels.not_null(task.id, "id")
        ValidatorModels.is_positive_integer(task.id, "id")
        # validaciones de title
        ValidatorModels.not_empty(task.title, "title")
        ValidatorModels.min_length(task.title, "title", 4)
        ValidatorModels.max_length(task.title, "title", 100)
        # validaciones de status
        ValidatorModels.not_empty(task.status, "status")
        ValidatorModels.min_length(task.status, "status", 4)
        ValidatorModels.max_length(task.status, "status", 20)
     
    def validate_id(id):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")
     

