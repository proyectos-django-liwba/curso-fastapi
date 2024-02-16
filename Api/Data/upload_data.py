# Dependencias
from sqlalchemy import Column,ForeignKey, Integer, String, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Models.upload_model import Upload
from Api.Models.user_model import User

class UploadData(ConexionBD.Base):
    __tablename__ = "uploads"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))
    
    def __str__(self):
        return f"Upload(id={self.id}, url={self.url}, user_id={self.user_id}, created_at={self.created_at}, updated_at={self.updated_at})"