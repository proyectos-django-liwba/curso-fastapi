# Dependencias
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Controllers.task_controller import TaskController
from Api.Models.task_model import Task
from Api.Models.examples import task_example_create, task_example_update
from Core.Enums.task_enum import StatusType

# Crear el router
task_router = APIRouter()

# Definir rutas
@task_router.post("/")
def create_task(task: Task = Body(example=task_example_create), db: Session = Depends(ConexionBD().get_db)):
    return TaskController.create_task(task, db)

@task_router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
   return TaskController.get_task(task_id, db)

@task_router.get("/")
def get_all_tasks(db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_all_tasks(db)

@task_router.get("/by_status/{status}")
def get_tasks_by_status(status: StatusType, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_tasks_by_status(status, db)

@task_router.put("/")
def update_task(task: Task = Body(example=task_example_update), db: Session = Depends(ConexionBD().get_db)):
    return TaskController.update_task(task, db)

@task_router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.delete_task(task_id, db)

@task_router.get("/{page}/{size}")
def paginate_tasks(page: int, size: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.paginate_tasks(page, size, db)