# Dependencias
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD


class UserData(ConexionBD.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
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

    def __str__(self):
        return f"User: ( id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, role={self.role}, verified={self.verified}, is_active={self.is_active}, otp={self.otp}, created_at={self.created_at}, updated_at={self.updated_at} )"