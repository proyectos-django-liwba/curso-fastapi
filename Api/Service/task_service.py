# Dependencias
from fastapi import Depends
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.task_data import TaskData
from Api.Models.task_model import Task
from Core.Validations.error import CustomError



class TaskService:
        
    def create_task(task: Task, db: Session ):

        _task = TaskData.create_task(task)
        
        db.add(_task)
        db.commit()
        db.refresh(_task)
        return _task
    
    def getTask(id: int, db: Session):
        result = db.query(TaskData).filter(TaskData.id == id).first()
       
        if result is None:
            raise CustomError(404, "Task not found")
        
        return result
    
    
    def get_all_tasks(db: Session):
        return db.query(TaskData).all()
    
    def update_task(id: int, task: Task, db: Session):
      
        _task = db.query(TaskData).filter(TaskData.id == id).first()
 
        if _task is None:
            raise CustomError(404, "Task not found")
        
        _task.title = task.title
        _task.status = task.status

        db.commit()
        return task
    
    def delete_task(id: int, db: Session):
        _task = db.query(TaskData).filter(TaskData.id == id).first()
 
        if _task is None:
            raise CustomError(404, "Task not found")
        
        db.delete(_task)
        db.commit()
        return {"message": "Task deleted successfully"}