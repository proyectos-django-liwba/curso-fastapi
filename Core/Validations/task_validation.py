from Core.Validations.validator_models import ValidatorModels
from Api.Models.task_model import Task

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
        # validaciones de category_task_id
        ValidatorModels.not_null(task.category_task_id, "category_task_id")
        ValidatorModels.is_positive_integer(task.category_task_id, "category_task_id")
        # validaciones de user_id
        ValidatorModels.not_null(task.user_id, "user_id")
        ValidatorModels.is_positive_integer(task.user_id, "user_id")
        
    def validate_update(task: Task):
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
        # validaciones de category_task_id
        ValidatorModels.not_null(task.category_task_id, "category_task_id")
        ValidatorModels.is_positive_integer(task.category_task_id, "category_task_id")
        # validaciones de user_id
        ValidatorModels.not_null(task.user_id, "user_id")
        ValidatorModels.is_positive_integer(task.user_id, "user_id")
     
    def validate_id(id: int):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")
        
        
    def validate_tags(task_id: int, tag_id: int):
        # validaciones de task_id
        ValidatorModels.not_null(task_id, "task_id")
        ValidatorModels.is_positive_integer(task_id, "task_id")
        # validaciones de tag_id
        ValidatorModels.not_null(tag_id, "tag_id")
        ValidatorModels.is_positive_integer(tag_id, "tag_id")
     

