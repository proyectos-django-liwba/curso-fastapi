# dependencias
from sqlalchemy.orm import Session
# importaciones
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Api.Service.task_service import TaskService
from Api.Models.task_model import Task
from Core.Validations.task_validation import TaskValidation
from Core.Pagination.pagination import paginate, PageParams

class TaskController: 
    
    def create_task(task: Task, db: Session):
        try:
            # validación de datos
            TaskValidation.validate_create(task)
            
            # Crear la tarea
            result = TaskService.create_task(task, db)
            
            # Retornar la respuesta
            return ResponseBase(201, "Task created successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al crear la tarea: ",{str(e)})
        
    def get_task(task_id: int, db: Session):
        try:
            # validar id
            TaskValidation.validate_id(task_id)
            
            result = TaskService.getTask(task_id, db)
            return ResponseBase(200, "Task obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al obtener la tarea: ",{str(e)})
    
    def get_all_tasks(db: Session):
        try:
            result = TaskService.get_all_tasks(db)
            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al listar las tareas: ",{str(e)})
    
    def get_tasks_by_status(status:str, db: Session):
        try:
            result = TaskService.get_tasks_by_status(status, db)
            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al listar las tareas: ",{str(e)})
    
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
            raise CustomError(500, "Error al actualizar la tarea: ",{str(e)})
    
    def delete_task(task_id: int, db: Session):
        try:
            # validar id
            TaskValidation.validate_id(task_id)
            
            TaskService.delete_task(task_id, db)
            return ResponseBase(200, "Task deleted successfully").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al eliminar la tarea: ", {str(e)})
        
    def paginate_tasks(page: int, size: int, db: Session):
        try:
            
            result = TaskService.paginate_tasks(page, size, PageParams, paginate, db)

            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al listar las tareas: ",{str(e)})
        
        
    # tablas intermedias
    
    def add_tag(task_id: int, tag_id: int, db: Session):
        try:
            # validación de datos
            TaskValidation.validate_tags(task_id, tag_id)
            
            # agregar tag
            result = TaskService.add_tag(task_id, tag_id, db)
            
            # Retornar la respuesta
            return ResponseBase(200, "Tag added successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al agregar el tag: ",{str(e)})
        
        
    def remove_tag(task_id: int, tag_id: int, db: Session):
        try:
            # validación de datos
            TaskValidation.validate_tags(task_id, tag_id)
            
            # eliminar tag
            result = TaskService.remove_tag(task_id, tag_id, db)
            
            # Retornar la respuesta
            return ResponseBase(200, "Tag removed successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al eliminar el tag: ",{str(e)})
        
    def get_task_with_tags(task_id: int, db: Session):
        try:
            # validar id
            TaskValidation.validate_id(task_id)
            
            result = TaskService.get_task_with_tags(task_id, db)
            return ResponseBase(200, "Task obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al obtener la tarea: ",{str(e)})
        
        
    def get_all_tasks_with_tags(db: Session):
        try:
            result = TaskService.get_all_tasks_with_tags(db)
            return ResponseBase(200, "Tasks obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error al listar las tareas: ",{str(e)})