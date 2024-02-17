# Dependencias
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Data.pivot_data import tasks_tags

class TagData(ConexionBD.Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    
    # relacion many to many, con tabla intermedia o pivote 
    tasks = relationship("TaskData", secondary=tasks_tags, back_populates="tags")
    
    
    def __str__(self):
        return f"Tag(id={self.id}, name={self.name})"