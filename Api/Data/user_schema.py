# Dependencias
from sqlalchemy import Column, Integer, String, Enum, Boolean, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD

class UserSchema(ConexionBD.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(100))
    role = Column(String(20), default="user")
    verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    otp = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"), onupdate=text("now()"))

    # def __str__(self):
    # return f"User: {self.username} - Email: {self.email} - Role: {self.role}"
