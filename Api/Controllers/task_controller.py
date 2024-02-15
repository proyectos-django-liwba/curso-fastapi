from sqlalchemy.orm import Session
from Api.Service.task_service import TaskService
from Api.Models.task_model import Task
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Core.Validations.task_validation import TaskValidation

class TaskController: 
    
    def create_task(task: Task, db: Session):
        try:
            # validación de datos
            TaskValidation.validate_create(task)
            
            # Crear la tarea
            result = TaskService.create_task(task, db)
            
            # Retornar la respuesta
            return ResponseBase(200, "Task created successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al crear la tarea: {str(e)}")
        
    def get_task(task_id: int, db: Session):
        try:
            # validar id
            TaskValidation.validate_id(task_id)
            
            result = TaskService.getTask(task_id, db)
            return ResponseBase(200, "Task obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al obtener la tarea: {str(e)}")
    
    def get_all_tasks(db: Session):
        try:
            result = TaskService.get_all_tasks(db)
            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al listar las tareas: {str(e)}")
    
    def get_tasks_by_status(status:str, db: Session):
        try:
            result = TaskService.get_tasks_by_status(status, db)
            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al listar las tareas: {str(e)}")
    
    def update_task( task: Task, db: Session):
        try:
            # validación de datos
            TaskValidation.validate_update(task)
            
            # Actualizar la tarea   
            result = TaskService.update_task(task, db)
            
            # Retornar la respuesta
            return ResponseBase(200, "Task updated successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al actualizar la tarea: {str(e)}")
    
    def delete_task(task_id: int, db: Session):
        try:
            # validar id
            TaskValidation.validate_id(task_id)
            
            TaskService.delete_task(task_id, db)
            return ResponseBase(200, "Task deleted successfully").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al eliminar la tarea: {str(e)}")