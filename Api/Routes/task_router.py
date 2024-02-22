# Dependencias
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Controllers.task_controller import TaskController
from Api.Models.task_model import Task
from Api.Models.examples import task_example_create, task_example_update
from Core.Enums.task_enum import StatusType
# socket
from fastapi import WebSocket, WebSocketDisconnect
from Core.Socket.socket_manager import WebSocketManager

# crear manager de websockets
manager = WebSocketManager()

# Crear el router
task_router = APIRouter()

@task_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    # Conectar cliente
    await manager.connect(websocket)
    
    await websocket.send_text(f"Welcome to the chat!")
    try:
        # Escuchar mensajes
        while True:
            
            
            # Recibir mensaje
            data = await websocket.receive_text()
            
            # Notificar cambios a los clientes
            
    except WebSocketDisconnect:
        # Desconectar cliente
        manager.disconnect(websocket)
        

# Definir rutas
@task_router.post("/")
def create_task(task: Task = Body(example=task_example_create), db: Session = Depends(ConexionBD().get_db)):
    return TaskController.create_task(task, db)

@task_router.get("/{task_id}/")
def get_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
   return TaskController.get_task(task_id, db)

@task_router.get("/")
def get_all_tasks(db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_all_tasks(db)

@task_router.get("/by_status/{status}/")
def get_tasks_by_status(status: StatusType, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_tasks_by_status(status, db)

@task_router.put("/")
def update_task(task: Task = Body(example=task_example_update), db: Session = Depends(ConexionBD().get_db)):
    return TaskController.update_task(task, db)

@task_router.delete("/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.delete_task(task_id, db)

# tablas intermedias
@task_router.get("/tasks_with_tags")
def get_all_tasks_with_tags(db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_all_tasks_with_tags(db)

@task_router.get("/with_tags/{task_id}/")
def get_task_with_tags(task_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.get_task_with_tags(task_id, db)


@task_router.post("/add_tag/{task_id}/{tag_id}/")
def add_tag(task_id: int, tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.add_tag(task_id, tag_id, db)

@task_router.delete("/remove_tag/{task_id}/{tag_id}/")
def remove_tag(task_id: int, tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.remove_tag(task_id, tag_id, db)

# paginación
@task_router.get("/{page}/{size}/")
def paginate_tasks(page: int, size: int, db: Session = Depends(ConexionBD().get_db)):
    return TaskController.paginate_tasks(page, size, db)



