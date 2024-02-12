from fastapi import APIRouter, Depends
from models.user_model import User
from domain.error import CustomError
from data.conection import ConexionBD
from data.user_schema import UserSchema


# Crear el router
user_router = APIRouter()

# Definir rutas
@user_router.post("/")
async def create_user(user: User):
    try:

        # Obtener la conexión y la sesión de la base de datos
        conexion = ConexionBD()
        db = conexion.get_Session()
        # Crear el objeto UserSchema con los datos del usuario
        db_user = UserSchema(**user.dict())

        # Agregar el usuario a la sesión y realizar la transacción
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        db.close()

        return db_user

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al crear el usuario: {str(e)}")
