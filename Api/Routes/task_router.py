# Dependencias
from fastapi import APIRouter, Body, HTTPException, status, Depends
from sqlalchemy.orm import Session
from Api.Data.conection import ConexionBD
# Importaciones
#from Core.Validations.error import CustomError
#from Api.Data.task_data import tasks_list
from Api.Controllers.task_controller import TaskController
from Api.Models.task_model import Task

# Crear el router
task_router = APIRouter()

# Definir rutas
@task_router.post("/")
def create_task(task: Task, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.create_task(task, db)

@task_router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
   return TaskController.get_task(task_id, db)

@task_router.get("/")
def get_all_tasks(db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_all_tasks(db)

@task_router.put("/{task_id}")
def update_task(task_id: int, task: Task, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.update_task(task_id, task, db)

@task_router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.delete_task(task_id, db)

