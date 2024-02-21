from Core.Security.security_auth import JWT
from Api.Service.user_service import UserService
from Core.Validations.custom_error import CustomError
from Core.Validations.user_validation import UserValidation
from Api.Data.conection import ConexionBD
from sqlalchemy.orm import Session
from typing import List

class Permission:
    
    def verify_role(token: str, role: List, db: Session) -> dict:
        # verificar token
        jwt = JWT()
        data_token =  jwt.verify_token(token)
        # verificar rol en bd
        
        user = UserService.get_user(data_token["user_id"], db)
        
        UserValidation.validate_user_exists(user)
        UserValidation.validate_user_verified(user)
        UserValidation.validate_user_active(user)
        
        if len(role) == 0:
            raise CustomError(500, "No se ha especificado un rol para verificar permisos")
        
        """ if user.role != role or data_token["role"] != role:
            raise CustomError(403, "No tienes permisos para realizar esta acción") """
        available = False
        for rol in role:
            if user.role == rol and data_token["role"] == rol:
                available = True
                break
            
        if not available:
            raise CustomError(403, "No tienes permisos para realizar esta acción")
        
        return {
            "user": user,
            "token": token,
        }
        
    