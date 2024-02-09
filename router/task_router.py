from fastapi import APIRouter, Body
from assets.enums.task_enum import StatusType
from models.task_model import Task

from data.task_data import tasks_list

# Crear el router
task_router = APIRouter()


# Definir rutas
@task_router.get("/")
def get_tasks():
  return {"tasks": tasks_list}

@task_router.post("/")
#def create_task(task: str, status: StatusType = StatusType.PENDING):
def create_task(task: Task = Body()):
  
  tasks_list.append( task )
  return {"task": tasks_list}

@task_router.get("/{index}")
def get_task(index: int):
  for i in range(len(tasks_list)):
    if i == index:
      return {"task": tasks_list[index]}
    
  return {"task": "Task not found"}

@task_router.put("/")
#def update_task(index: int, task: str, status: StatusType):
#def update_task(index: int, task: Task = Body()):
def update_task(index: int, task: Task ):
  tasks_list[index] = task
  return {"task": tasks_list}

@task_router.delete("/")
def delete_task(index: int):
  del tasks_list[index]
  return {"task": tasks_list}