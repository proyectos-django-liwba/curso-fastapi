
from Core.Emails.email import EmailManager
from fastapi import Depends, HTTPException
from Api.Data.conection import ConexionBD
from sqlalchemy.orm import Session
from Api.Models.user_model import User
from Api.Response.response_base import ResponseBase
from Api.Service.user_service import UserService
from Core.Validations.custom_error import CustomError
from Core.Security.security_encryption import SecurityEncryption
from Core.Security.security_auth import JWT
from Core.Validations.user_validation import UserValidation
class UserController:
    
    async def create_user(user: User, db: Session = Depends(ConexionBD().get_db)):
        try: 
            
            UserValidation.validate_create(user)
            otp = JWT().create_token({"sub": user.name},token_type="activate", expires_minutes=1440, role="user")
            print(otp)
            link = f"http://localhost:5173/{otp}"
            hashed_password = SecurityEncryption().hash_password(user.password)
            print(hashed_password)
            # Llama al método send_mail con la dirección de correo electrónico
            await EmailManager().send_email(user.email, "Registro de Usuario", user.name, link)
            result = UserService().create_user(db, user, hashed_password, otp)
            # Retorna la respuesta al cliente
            return ResponseBase(200, "Usuario registrado correctamente", result).to_dict()
            
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
"""  def login(request: RequestUserLogin, db: Session = Depends(ConexionBD().get_db)):
        try:
            return UserService().login_user(db, request.parameter.email, request.parameter.password)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
    def get_user_by_id(user_id: int, db: Session = Depends(ConexionBD().get_db)):
        try:
            users = UserService().get_user_by_id(db, user_id)
            print(users)
            return ResponseUserUpdate(code=200, status="success", message="Usuario obtenido correctamente", result=users).model_dump(exclude_none=True)
        except CustomError as e:
            raise e

        except Exception as e:
            return CustomError(500, f"Ocurrio un error inesperado, por favor vuelva a intentar mas tarde: {str(e)}")

    @staticmethod
    def get_user(db: Session = Depends(ConexionBD().get_db), skipt: int = 0, limit: int = 100):
        try:
            users = UserService().get_user(db, skipt, limit)
            return ResponseGetUser(code=200, status="success", message="Usuarios obtenidos correctamente", users=users)
        except CustomError as e:
            raise e
        except HTTPException as e:
            if e.status_code == 403:
                return CustomError(403, f"Error de permisos: {str(e)}")
                #como hago para que esta respuesta me la envie al frontend 
            elif e.status_code == 401:
                return CustomError(401, f"Error al autenticarse: {str(e)}")
        except Exception as e:
            return CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
    def update_user(user_id: int, request: RequestUserUpdate, db: Session = Depends(ConexionBD().get_db)):
        try:
            user = UserService().update_user(db, user_id, request.parameter)
            return ResponseUserUpdate(code=200, status="success", message="Usuario actualizado correctamente", result=user).model_dump(exclude_none=True)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")


 """