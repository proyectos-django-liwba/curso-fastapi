# Dependencias
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.task_data import TaskData
from Api.Models.task_model import Task
from Core.Validations.custom_error import CustomError



class TaskService:
        
    def create_task(task: Task, db: Session ):

        _task = TaskData.create_task(task)
        
        db.add(_task)
        db.commit()
        db.refresh(_task)
        return _task
    
    def getTask(id: int, db: Session):
        result = db.query(TaskData).get(id)
       
        if result is None:
            raise CustomError(404, "Task not found")
        
        return result
    
    def get_all_tasks(db: Session):
        return db.query(TaskData).all()
    
    def get_tasks_by_status(status: str, db: Session):
        return db.query(TaskData).filter(TaskData.status == status).all()
    
    def update_task( task: Task, db: Session):
      
        _task = db.query(TaskData).get(id)
 
        if _task is None:
            raise CustomError(404, "Task not found")
        
        _task.title = task.title
        _task.status = task.status

        db.commit()
        db.refresh(_task)
        # retorna el objeto con todos los atributos
        # puede ser necesario devolver solo algunos atributos
        return _task
    
    def delete_task(id: int, db: Session):
        _task = db.query(TaskData).get(id)
 
        if _task is None:
            raise CustomError(404, "Task not found")
        
        db.delete(_task)
        db.commit()
