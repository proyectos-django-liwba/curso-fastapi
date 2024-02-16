# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.category_tasks_model import CategoryTasks
from Api.Data.category_tasks_data import CategoryTasksData

class CategoryTasksService:
    
    def create_category_task(category_task: CategoryTasks, db: Session):
        _category_task = CategoryTasksData(name=category_task.name, description=category_task.description)
        
        try:
            db.add(_category_task)
            db.commit()
            db.refresh(_category_task)
            return _category_task
        
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    
    def get_category_task(id: int, db: Session):
        result = db.query(CategoryTasksData).get(id)
       
        if result is None:
            raise CustomError(404, "CategoryTask not found")
        
        return result
    
    def get_all_category_tasks(db: Session):
        return db.query(CategoryTasksData).all()
    
    def update_category_task(category_task: CategoryTasks, db: Session):
      
        _category_task = db.query(CategoryTasksData).get(category_task.id)

        if _category_task is None:
            raise CustomError(404, "CategoryTask not found")
        
        try: 
            _category_task.name = category_task.name
            _category_task.description = category_task.description

            db.commit()
            db.refresh(_category_task)

            return _category_task
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    def delete_category_task(id: int, db: Session):
        _category_task = db.query(CategoryTasksData).get(id)
 
        if _category_task is None:
            raise CustomError(404, "CategoryTask not found")
        
        db.delete(_category_task)
        db.commit()
        