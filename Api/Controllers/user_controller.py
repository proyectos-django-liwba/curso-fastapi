# dependencias
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
# importaciones
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Api.Service.user_service import UserService
from Api.Models.user_model import User
from Core.Validations.user_validation import UserValidation
from Core.Emails.email import EmailManager
from Core.Security.security_auth import JWT
from Core.Security.security_encryption import SecurityEncryption
from Core.Validations.user_validation import UserValidation


class UserController:
    
    async def create_user(user: User, db: Session, background_tasks: BackgroundTasks):
        try:

            # validar datos
            UserValidation.validate_create(user)
            otp = JWT().create_otp({"sub": "123456"},token_type="activate", expires_minutes=1440)
            link = f"http://localhost:5173/{otp}"
            

            # enviar correo
            """ email_manager = EmailManager()
            await email_manager.send_email(
                user.email, "Registro de Usuario", user.first_name, link
            ) """
            #BackgroundTasks.add_task(EmailManager().send_email, user.email, "Registro de Usuario", user.first_name, link)
            
            background_tasks.add_task(
                EmailManager().send_email,
                user.email,
                "Registro de Usuario",
                user.first_name,
                link
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
            UserValidation.validate_login(user)
            user2 = UserService.login_user(user.email, user.password, db)
            
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
        
    def change_password(id, password,new_password, confirm_password, db: Session):
        try:
            
            UserValidation.validate_change_password(id, password, new_password, confirm_password)
            UserValidation.validate_password_equal(new_password, confirm_password)
            new_password = SecurityEncryption().hash_password(new_password)
            UserService.change_password(id, password, new_password, db)
            return ResponseBase(200, "Contraseña cambiada correctamnte").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error changing password: {str(e)}")
        
    
    def activate_user(user: User, db: Session):
        try:

            UserService.activate_user(user.otp, db)
            return ResponseBase(200, "Usuario activado correctamente").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error activating user: {str(e)}")
        
    def verify_account(user: User, db: Session):
        try:
            user = UserService.verify_user(user.otp, db)
            print(user)
            return ResponseBase(200, "Usuario verificado correctamente").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error verifying user: {str(e)}")
        
    def get_user_not_verified(db: Session):
        try:
            result = UserService.get_user_not_verified(db)
            return ResponseBase(200, "Usuarios no verificados", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error getting not verify users: {str(e)}")
        
        
    def forgot_password(email, db: Session, background_tasks: BackgroundTasks):
        try:
            otp = JWT().create_otp({"sub": "123456"},token_type="forgot-password", expires_minutes=1440)
            user2 = UserService.forgot_password(email,otp, db)
            
            link = f"http://localhost:5173/forgot-password/{otp}"
            background_tasks.add_task(
                EmailManager().send_email,
                user2.email,
                "Recuperación de contraseña",
                user2.first_name,
                link,
                2
            )
            
            return ResponseBase(200, "Correo enviado correctamente").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error sending email: {str(e)}")
        
        
    def desactivate_account(id, db: Session):
        try:
            UserService.desactivate_account(id, db)
            return ResponseBase(200, "Usuario desactivado correctamente").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error desactivating user: {str(e)}")
        
    def reset_password(otp, password, confirm_password, db: Session):
        try:
            UserValidation.validate_password(password,confirm_password)
            password = SecurityEncryption().hash_password(password)
            UserService.reset_password(otp, password, db)
            return ResponseBase(200, "Contraseña cambiada correctamente").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error reseting password: {str(e)}")