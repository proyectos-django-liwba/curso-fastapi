from Core.Validations.validator_models import ValidatorModels
from Api.Models.category_tasks_model import CategoryTasks

class CategoryTasksValidation:
    
    def validate_create(category_task: CategoryTasks):
        # validaciones de title
        ValidatorModels.not_empty(category_task.name, "name")
        ValidatorModels.min_length(category_task.name, "name", 4)
        ValidatorModels.max_length(category_task.name, "name", 100)
        # validaciones de description
        ValidatorModels.not_empty(category_task.description, "description")
        ValidatorModels.min_length(category_task.description, "description", 4)
        ValidatorModels.max_length(category_task.description, "description", 300)
        
    def validate_update(category_task: CategoryTasks):
        # validaciones de id
        ValidatorModels.not_null(category_task.id, "id")
        ValidatorModels.is_positive_integer(category_task.id, "id")
        # validaciones de title
        ValidatorModels.not_empty(category_task.name, "name")
        ValidatorModels.min_length(category_task.name, "name", 4)
        ValidatorModels.max_length(category_task.name, "name", 100)
        # validaciones de description
        ValidatorModels.not_empty(category_task.description, "description")
        ValidatorModels.min_length(category_task.description, "description", 4)
        ValidatorModels.max_length(category_task.description, "description", 300)
     
    def validate_id(id: int):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")