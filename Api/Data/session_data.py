# Dependencias
from sqlalchemy import Column, BigInteger, String, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD

class SessionData(ConexionBD.Base):
    __tablename__ = "sessions"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True, nullable=False)
    token = Column(String(200), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))

    def __str__(self):
        return f"Session: ( id={self.id}, user_id={self.user_id}, token={self.token}, is_active={self.is_active}, created_at={self.created_at}, updated_at={self.updated_at} )"