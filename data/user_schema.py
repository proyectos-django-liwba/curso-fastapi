from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Enum

from data.conection import ConexionBD

conection = ConexionBD()

class UserSchema( conection.get_base() ):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(16))
    role = Column(Enum("admin", "user", name="role_types"))

    #def __str__(self):
        #return f"User: {self.username} - Email: {self.email} - Role: {self.role}"