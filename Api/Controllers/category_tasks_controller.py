# dependencias
from sqlalchemy.orm import Session
# importaciones
from Api.Service.category_tasks_service import CategoryTasksService
from Api.Models.category_tasks_model import CategoryTasks
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Core.Validations.category_tasks_validation import CategoryTasksValidation

class CategoryTasksController:
    
    def create_category_task(category_task: CategoryTasks, db: Session):
        try:
            # validar datos
            CategoryTasksValidation.validate_create(category_task)
            # crear category_task
            result = CategoryTasksService.create_category_task(category_task, db)
            # retornar respuesta
            return ResponseBase(201, "CategoryTask created", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error creating category_task: ",{str(e)})
        
    def get_category_task(id: int, db: Session):
        try:
            # validar datos
            CategoryTasksValidation.validate_id(id)
            # buscar category_task
            result = CategoryTasksService.get_category_task(id, db)
            # retornar respuesta
            return ResponseBase(200, "CategoryTask found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error getting category_task: ",{str(e)})
        
        
    def get_all_category_tasks(db: Session):
        try:
            # buscar category_tasks
            result = CategoryTasksService.get_all_category_tasks(db)
            # retornar respuesta
            return ResponseBase(200, "CategoryTasks found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error getting category_tasks: ",{str(e)})
        
    def update_category_task(category_task: CategoryTasks, db: Session):
        try:
            # validar datos
            CategoryTasksValidation.validate_id(category_task.id)
            # actualizar category_task
            result = CategoryTasksValidation.validate_update(category_task)
            # retornar respuesta
            return ResponseBase(200, "CategoryTask updated", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error updating category_task: ",{str(e)})
    
    def delete_category_task(id: int, db: Session):
        try:
            # validar datos
            CategoryTasksValidation.validate_id(id)
            # eliminar category_task
            CategoryTasksService.delete_category_task(id, db)
            # retornar respuesta
            return ResponseBase(200, "CategoryTask deleted").to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error deleting category_task: ",{str(e)})
    