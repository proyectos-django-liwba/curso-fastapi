# Dependencias
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Controllers.category_tasks_controller import CategoryTasksController
from Api.Models.category_tasks_model import CategoryTasks
from Api.Models.examples import category_tasks_example_create, category_tasks_example_update

# Crear el router
category_tasks_router = APIRouter()

# Definir rutas
@category_tasks_router.post("/")
def create_category_task(category_task: CategoryTasks = Body(example=category_tasks_example_create), db: Session = Depends(ConexionBD().get_db)):
    return CategoryTasksController.create_category_task(category_task, db)

@category_tasks_router.get("/{category_task_id}")
def get_category_task(category_task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return CategoryTasksController.get_category_task(category_task_id, db)

@category_tasks_router.get("/")
def get_all_category_tasks(db: Session = Depends(ConexionBD().get_db)):
    return CategoryTasksController.get_all_category_tasks(db)

@category_tasks_router.put("/")
def update_category_task(category_task: CategoryTasks = Body(example=category_tasks_example_update), db: Session = Depends(ConexionBD().get_db)):
    return CategoryTasksController.update_category_task(category_task, db)

@category_tasks_router.delete("/{category_task_id}")
def delete_category_task(category_task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return CategoryTasksController.delete_category_task(category_task_id, db)