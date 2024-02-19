# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Data.task_data import TaskData
from Api.Models.task_model import Task
from Api.Data.tag_data import TagData

class TaskService:
        
    def create_task(task: Task, db: Session ):

        _task = TaskData(title=task.title, status=task.status, category_task_id=task.category_task_id, user_id=task.user_id)
        
        try: 
            db.add(_task)
            db.commit()
            db.refresh(_task)
            return _task
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    def getTask(id: int, db: Session):
        result = db.query(TaskData).get(id)
       
        if result is None:
            raise CustomError(404, "Task not found")
        
        return result
    
    def get_all_tasks(db: Session):
        return db.query(TaskData).order_by(TaskData.id).all()
    
    def get_tasks_by_status(status: str, db: Session):
        return db.query(TaskData).order_by(TaskData.id).filter(TaskData.status == status).all()
    
    def update_task( task: Task, db: Session):
      
        _task = db.query(TaskData).get(task.id)

        if _task is None:
            raise CustomError(404, "Task not found")
        try: 
            _task.title = task.title
            _task.status = task.status
            _task.category_task_id = task.category_task_id
            _task.user_id = task.user_id

            db.commit()
            db.refresh(_task)
            return _task
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    
    def delete_task(id: int, db: Session):
        _task = db.query(TaskData).get(id)
 
        if _task is None:
            raise CustomError(404, "Task not found")
        
        db.delete(_task)
        db.commit()

    def paginate_tasks(page: int, size: int,PageParams: dict, paginate: callable, db: Session):
        # inicializar el objeto de paginación
        page_params = PageParams(page=page, size=size)
        
        # retornar el resultado de la paginación
        return paginate(page_params, db.query(TaskData), Task)
    
    
    # tablas intermedias

    def add_tag(task_id: int, tag_id: int, db: Session):
        _task = db.query(TaskData).get(task_id)
        if _task is None:
            raise CustomError(404, "Task not found")

        _tag = db.query(TagData).get(tag_id)
        if _tag is None:
            raise CustomError(404, "Tag not found")
        
        try: 
            _task.tags.append(_tag)
            db.commit()
            db.refresh(_task)
            
            return {
                "id": _task.id,
                "title": _task.title,
                "status": _task.status,
                "category_task_id": _task.category_task_id,
                "user_id": _task.user_id,
                "tags": _task.tags
            }

        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    def remove_tag(task_id: int, tag_id: int, db: Session):
        _task = db.query(TaskData).get(task_id)
        if _task is None:
            raise CustomError(404, "Task not found")

        _tag = db.query(TagData).get(tag_id)
        if _tag is None:
            raise CustomError(404, "Tag not found")
        
        if _tag not in _task.tags:
            raise CustomError(404, "Tag not found in task")
        
        try: 
            _task.tags.remove(_tag)
            db.commit()
            db.refresh(_task)
            return {
                "id": _task.id,
                "title": _task.title,
                "status": _task.status,
                "category_task_id": _task.category_task_id,
                "user_id": _task.user_id,
                "tags": _task.tags
            }
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
        
        
    def get_task_with_tags(task_id: int, db: Session):
        _task = db.query(TaskData).get(task_id)
        
        if _task is None:
            raise CustomError(404, "Task not found")
        
        return {
            "id": _task.id,
            "title": _task.title,
            "status": _task.status,
            "category_task_id": _task.category_task_id,
            "user_id": _task.user_id,
            "tags": sorted(_task.tags, key=lambda tag: tag.id)
        }
        
        
    def get_all_tasks_with_tags(db: Session):
        _tasks = db.query(TaskData).all()
        
        result = []
        for _task in _tasks:
            
            # order las tags por id
            sorted_tags = sorted(_task.tags, key=lambda tag: tag.id)
        
            result.append({
                "id": _task.id,
                "title": _task.title,
                "status": _task.status,
                "category_task_id": _task.category_task_id,
                "user_id": _task.user_id,
                "tags": sorted_tags
            })
        
        return result