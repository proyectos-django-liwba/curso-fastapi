from fastapi import APIRouter, Body, HTTPException, status
from models.task_model import Task
from domain.error import CustomError

# Importar datos
from data.task_data import tasks_list

# Crear el router
task_router = APIRouter()


# Definir rutas
@task_router.get("/", status_code=status.HTTP_200_OK)
def get_tasks():
    return {"tasks": tasks_list}


@task_router.post("/", status_code=status.HTTP_201_CREATED)
# def create_task(task: str, status: StatusType = StatusType.PENDING):
def create_task(task: Task = Body()):

    tasks_list.append(task)
    return {"task": tasks_list}


@task_router.get("/{index}", status_code=status.HTTP_200_OK)
def get_task(index: int):
    for i in range(len(tasks_list)):
        if i == index:
            return {"task": tasks_list[index]}

    return {"task": "Task not found"}


@task_router.put("/", status_code=status.HTTP_200_OK)
# def update_task(index: int, task: str, status: StatusType):
# def update_task(index: int, task: Task = Body()):
def update_task(index: int, task: Task):
    tasks_list[index] = task
    return {"task": tasks_list}


@task_router.delete("/")
def delete_task(index: int):

  try:
    if len(tasks_list) <= index:
        raise CustomError(404, "Tarea no encontrada")
      
    del tasks_list[index]
    return {"task": tasks_list}
  
  except Exception as e:
    raise CustomError(500, f"Error al eliminar la tarea: {e}")


#manejo de errores
# raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found" )
# raise JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Not found", "error": "Tarea no encontrada"})
""" raise HTTPException(
  status_code=status.HTTP_404_NOT_FOUND,
  detail={"type": "Not found", "error": "Tarea no encontrada"},
) """