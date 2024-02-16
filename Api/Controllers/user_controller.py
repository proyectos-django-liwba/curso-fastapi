from sqlalchemy.orm import Session
from Api.Service.user_service import UserService
from Api.Models.user_model import User
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Core.Validations.user_validation import UserValidation
from Core.Emails.email import EmailManager
from passlib.context import CryptContext

class UserController:
    
    async def create_user(user: User, db: Session):
        try:

            # validar datos
            UserValidation.validate_create(user)
            
            # envio de correo
            otp = "1da-sd22DA-SDAD-A3DASDA-4"
            link = f"http://localhost:5173/{otp}"

            # enviar correo
            email_manager = EmailManager()
            await email_manager.send_email(
                user.email, "Registro de Usuario", user.first_name, link
            )
            
            # Configura el contexto de cifrado sin especificar el esquema
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

            # hash de la contraseña
            hashed_password = pwd_context.hash(user.password)
            user.password = hashed_password
            
            # crear user
            result = UserService.create_user(user, db)
            # retornar respuesta
            return ResponseBase(201, "User created", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error creating user: {str(e)}")
        
    def get_user(id: int, db: Session):
        try:
            # validar datos
            UserValidation.validate_id(id)
            # buscar user
            result = UserService.get_user(id, db)
            # retornar respuesta
            return ResponseBase(200, "User found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error getting user: {str(e)}")
        
        
    def get_all_users(db: Session):
        try:
            # buscar users
            result = UserService.get_all_users(db)
            # retornar respuesta
            return ResponseBase(200, "Users found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error getting users: {str(e)}")
        
    def update_user(user: User, db: Session):
        try:
            
            # validar datos
            UserValidation.validate_update(user)
            
            # actualizar user
            result = UserService.update_user(user, db)
            # retornar respuesta
            return ResponseBase(200, "User updated", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error updating user: {str(e)}")
        
        
    def delete_user(id: int, db: Session):
        try:
            # validar datos
            UserValidation.validate_id(id)
            # eliminar user
            result = UserService.delete_user(id, db)
            # retornar respuesta
            return ResponseBase(200, "User deleted", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error deleting user: {str(e)}")
