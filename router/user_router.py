from fastapi import APIRouter, Depends
from models.user_model import User
from domain.error import CustomError
from data.conection import ConexionBD
from data.user_schema import UserSchema
from sqlalchemy.orm import Session
from emails.email import EmailManager
from passlib.context import CryptContext

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
