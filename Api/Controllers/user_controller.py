# dependencias
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# importaciones
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Api.Service.user_service import UserService
from Api.Models.user_model import User
from Core.Validations.user_validation import UserValidation
from Core.Emails.email import EmailManager
from Core.Security.security_auth import JWT
from Core.Security.security_encryption import SecurityEncryption

class UserController:
    
    async def create_user(user: User, db: Session):
        try:

            # validar datos
            UserValidation.validate_create(user)
            otp = JWT().create_otp({"sub": "123456"},token_type="activate", expires_minutes=1440)
            link = f"http://localhost:5173/{otp}"
            

            # enviar correo
            email_manager = EmailManager()
            await email_manager.send_email(
                user.email, "Registro de Usuario", user.first_name, link
            )
            
            user.password = SecurityEncryption().hash_password(user.password)
            user.otp = otp
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
            UserService.delete_user(id, db)
            # retornar respuesta
            return ResponseBase(200, "User deleted").to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error deleting user: {str(e)}")

    def login_user(user: User, db: Session):
        try:
            user_password = user.password
            user_email = user.email
            user2 = UserService.login_user(user_email, user_password, db)
            
            token = JWT().create_token({"sub": "123456"}, token_type="access", role=user2["role"], user_id=user2["id"])
            result = {
                "user": user2,
                "access": token
            }
            
            return ResponseBase(200, "Logueado correctamente", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        