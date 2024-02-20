# Dependencias
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, text
from sqlalchemy.orm import relationship
# Importaciones
from .conection import ConexionBD

class CategoryTasksData( ConexionBD.Base):
    __tablename__ = "category_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))
    
    # relacion one to many inversa
    #tasks = relationship("TaskData",lazy="joined", back_populates="category_task")
    
    def __str__(self):
        return f"CategoryTask(id={self.id}, name={self.name}, description={self.description}, created_at={self.created_at}, updated_at={self.updated_at})"