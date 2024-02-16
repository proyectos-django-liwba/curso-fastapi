from sqlalchemy.orm import Session
from Api.Service.category_tasks_service import CategoryTasksService
from Api.Models.category_tasks_model import CategoryTasks
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Core.Validations.category_tasks_validation import CategoryTasksValidation


class CategoryTasksController:
    
    def create_category_task(category_task: CategoryTasks, db: Session):
        # validar datos
        CategoryTasksValidation.validate_create(category_task)
        # crear category_task
        result = CategoryTasksService.create_category_task(category_task, db)
        # retornar respuesta
        return ResponseBase(201, "CategoryTask created", result).to_dict()
    
    def get_category_task(id: int, db: Session):
        # validar datos
        CategoryTasksValidation.validate_id(id)
        # buscar category_task
        result = CategoryTasksService.get_category_task(id, db)
        # retornar respuesta
        return ResponseBase(200, "CategoryTask found", result).to_dict()
    
    def get_all_category_tasks(db: Session):
        # buscar category_tasks
        result = CategoryTasksService.get_all_category_tasks(db)
        # retornar respuesta
        return ResponseBase(200, "CategoryTasks found", result).to_dict()
    
    def update_category_task(category_task: CategoryTasks, db: Session):
        # validar datos
        CategoryTasksValidation.validate_id(category_task.id)
        # actualizar category_task
        result = CategoryTasksValidation.validate_update(category_task)
        # retornar respuesta
        return ResponseBase(200, "CategoryTask updated", result).to_dict()
    
    def delete_category_task(id: int, db: Session):
        # validar datos
        CategoryTasksValidation.validate_id(id)
        # eliminar category_task
        CategoryTasksService.delete_category_task(id, db)
        # retornar respuesta
        return ResponseBase(200, "CategoryTask deleted").to_dict()
    