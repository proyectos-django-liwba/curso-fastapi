# Dependencias
from sqlalchemy import Column,ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Data.pivot_data import tasks_tags

class TaskData(ConexionBD.Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    status = Column(String(20), default="PENDING")
    
    # relacion one to many
    category_task_id = Column(Integer, ForeignKey("category_tasks.id"), nullable=False)
    category_task= relationship("CategoryTasksData", lazy="joined")
    
    # relacion one to many inversa
    #category_task= relationship("CategoryTasksData", lazy="joined", back_populates="tasks")
    
    # relacion one to many
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user= relationship("UserData", lazy="joined")
    
    # relacion many to many, con tabla intermedia o pivote 
    tags = relationship("TagData", secondary=tasks_tags, back_populates="tasks")
    
    # datos de creacion y actualizacion
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))
    
    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"
