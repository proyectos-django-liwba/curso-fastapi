# Dependencias
from sqlalchemy import Column, Integer, String, Enum, Boolean, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Models.task_model import Task

class TaskData(ConexionBD.Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    status = Column(String(20), default="PENDING")
    #category_id = Column(Integer)
    #user_id = Column(Integer)
    #created_at = Column(TIMESTAMP, server_default=text("now()"))
    #updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))

    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"


    def create_task(task: Task):
        return TaskData(title=task.title, status=task.status)


""" # Almacenar tareas
tasks_list = [
    {
        "id": 1,
        "title": "Limpiar la casa",
        "status": StatusType.DONE,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
    {
        "id": 2,
        "title": "Hacer la compra",
        "status": StatusType.PENDING,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
    {
        "id": 3,
        "title": "Cocinar la cena",
        "status": StatusType.PENDING,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
]
 """