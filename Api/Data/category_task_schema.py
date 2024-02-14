# Dependencias
from sqlalchemy import Column, Integer, String, Text
# Importaciones
from .conection import ConexionBD

class CategoryTaskSchema( ConexionBD.Base):
    __tablename__ = "category_task"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    description = Column(Text, nullable=True)
    