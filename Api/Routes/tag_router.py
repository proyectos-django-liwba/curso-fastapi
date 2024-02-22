# Dependencias
from fastapi import APIRouter, Depends, Body 
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Controllers.tag_controller import TagController
from Api.Models.tag_model import Tag
from Api.Models.examples import tag_example_create, tag_example_update
# socket
from fastapi import WebSocket, WebSocketDisconnect, Header, BackgroundTasks
from Core.Socket.socket_manager import WebSocketManager
from Core.Security.security_permissions import Permission
import json

# Crear router
tag_router = APIRouter()

# Autorización
def validate_auth( bearer: str = Header(), db: Session = Depends(ConexionBD().get_db)):
   return Permission.verify_role(bearer, ["admin", "user"], db)

# crear manager de websockets
manager = WebSocketManager()

# definir rutas de websockets
@tag_router.websocket("/ws", dependencies=[Depends(validate_auth)])
async def websocket_endpoint(websocket: WebSocket, user_data: dict = Depends(validate_auth)):
    
    # Conectar cliente
    await manager.connect(websocket)
    
    # Enviar mensaje de bienvenida
    await websocket.send_text(f"Welcome to the socket module tags: {user_data['user'].first_name}")
    print(f"usuarios conectados: {len(manager.connections)}")
    
    try:
        # Escuchar mensajes
        while True:
            
            # Recibir mensaje
            data = await websocket.receive_text()
            print(data)
            
            # Notificar cambios a los clientes
            if data is not None:
                await manager.broadcast(data)
            
    except WebSocketDisconnect:
        # Desconectar cliente
        manager.disconnect(websocket)
        print(f"usuarios conectados: {len(manager.connections)}")
        

# definir rutas de tags
@tag_router.post("/")
def create_tag(background_task: BackgroundTasks,  tag: Tag = Body(example=tag_example_create), db: Session = Depends(ConexionBD().get_db)):
    result = TagController.create_tag(tag, db)
    
    if result:
        print("enviando mensaje a los clientes")
        notification_data = {"action": "Create", "module": "tag"}
        background_task.add_task(manager.broadcast, json.dumps(notification_data))
        #background_task.add_task(manager.broadcast, "Se ha creado un nuevo tag")
    
    return result

@tag_router.get("/{tag_id}")
def get_tag(tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TagController.get_tag(tag_id, db)

@tag_router.get("/")
def get_all_tags(db: Session = Depends(ConexionBD().get_db)):
    return TagController.get_all_tags(db)

@tag_router.put("/")
def update_tag(background_task: BackgroundTasks, tag: Tag = Body(example=tag_example_update), db: Session = Depends(ConexionBD().get_db)):
    result = TagController.update_tag(tag, db)
    
    if result:
        print("enviando mensaje a los clientes")
        notification_data = {"action": "Update", "module": "tag"}
        background_task.add_task(manager.broadcast, json.dumps(notification_data))

    return result 

@tag_router.delete("/{tag_id}")
def delete_tag(background_task: BackgroundTasks, tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    result = TagController.delete_tag(tag_id, db)

    if result:
        print("enviando mensaje a los clientes")
        notification_data = {"action": "Delete", "module": "tag"}
        background_task.add_task(manager.broadcast, json.dumps(notification_data))
   
    return result 
