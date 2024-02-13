from fastapi import APIRouter, Depends
from models.user_model import User
from domain.error import CustomError
from data.conection import ConexionBD
from data.user_schema import UserSchema
from sqlalchemy.orm import Session
from emails.email import EmailManager
from passlib.context import CryptContext
from sqlalchemy import text

# Crear el router
user_router = APIRouter()

# Configura el contexto de cifrado sin especificar el esquema
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Definir rutas
@user_router.post("/")
async def create_user(user: User, db: Session = Depends(ConexionBD().get_db)):
    try:

        # envio de correo
        otp = "1da-sd22DA-SDAD-A3DASDA-4"
        link = f"http://localhost:5173/{otp}"

        # enviar correo
        email_manager = EmailManager()
        await email_manager.send_email(
            user.email, "Registro de Usuario", user.username, link
        )

        # hash de la contraseña
        hashed_password = pwd_context.hash(user.password)

        _user = UserSchema(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_password,
        )

        db.add(_user)
        db.commit()
        db.refresh(_user)

        return {
            "user": {
                "id": _user.id,
                "username": _user.username,
                "first_name": _user.first_name,
                "last_name": _user.last_name,
                "email": _user.email,
                "role": _user.role,
            }
        }

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al crear el usuario: {str(e)}")


@user_router.get("/by_sql")
async def get_users(db: Session = Depends(ConexionBD().get_db)):
    try:
        # Ejecutar la consulta sql
        result = db.execute(
            text("SELECT id, username, first_name, last_name, email, role from users")
        )

        users = []
        for row in result:
            user_data = {
                "id": row[0],
                "username": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "email": row[4],
                "role": row[5],
            }
            users.append(user_data)

        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")

@user_router.get("/by_bd_function")
async def get_users(db: Session = Depends(ConexionBD().get_db)):
    try:
        # Ejecutar la consulta sql
        result = db.execute(
            text("SELECT * FROM obtener_usuarios();")
        )

        users = []
        for row in result:
            user_data = {
                "id": row[0],
                "username": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "email": row[4],
                "role": row[5],
            }
            users.append(user_data)

        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")


@user_router.get("/by_orm")
async def get_user(db: Session = Depends(ConexionBD().get_db)):
    try:

        users = db.query(UserSchema).all()
        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")

@user_router.get("/by_id/{user_id}")
async def get_user(user_id: int ,db: Session = Depends(ConexionBD().get_db)):
    try:
        
        if user_id is None:
            raise CustomError(400, "El id del usuario es requerido")
        
        if user_id <= 0:
            raise CustomError(400, "El id del usuario debe ser mayor a 0")
        
        user = db.query(UserSchema).filter(UserSchema.id == user_id).first()

        if user is None:
            raise CustomError(404, "Usuario no encontrado")
       
        return {"user": user}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")
