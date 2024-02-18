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
    
    def update_task(task: Task):
        return TaskData(id=task.id, title=task.title, status=task.status)
