from Core.Validations.validator_models import ValidatorModels
from Api.Models.user_model import User
from Core.Validations.custom_error import CustomError
from Core.Security.security_encryption import SecurityEncryption
class UserValidation: 
    
    def validate_create(user: User):
        # validaciones de first_name
        ValidatorModels.not_null(user.first_name, "first_name")
        ValidatorModels.not_empty(user.first_name, "first_name")
        ValidatorModels.min_length(user.first_name, "last_name", 3)
        ValidatorModels.max_length(user.first_name, "last_name", 50)
        # validaciones de last_name
        ValidatorModels.not_null(user.last_name, "last_name")
        ValidatorModels.not_empty(user.last_name, "last_name")
        ValidatorModels.min_length(user.last_name, "last_name", 3)
        ValidatorModels.max_length(user.last_name, "last_name", 50)
        # validaciones de email
        ValidatorModels.not_null(user.email, "email")
        ValidatorModels.not_empty(user.email, "email")
        ValidatorModels.is_email(user.email, "email")
        # validaciones de password
        ValidatorModels.not_null(user.password, "password")
        ValidatorModels.not_empty(user.password, "password")
        ValidatorModels.is_password(user.password, "password")
        ValidatorModels.min_length(user.password, "password", 8)
        ValidatorModels.max_length(user.password, "password", 16)

    def validate_update(user: User):
        # validaciones de id
        ValidatorModels.not_null(user.id, "id")
        ValidatorModels.is_positive_integer(user.id, "id")
        # validaciones de first_name
        ValidatorModels.not_null(user.first_name, "first_name")
        ValidatorModels.not_empty(user.first_name, "first_name")
        print(user.first_name)
        ValidatorModels.min_length(user.first_name,"last_name", 3)
        ValidatorModels.max_length(user.first_name,"last_name", 50)
        # validaciones de last_name
        ValidatorModels.not_null(user.last_name, "last_name")
        ValidatorModels.not_empty(user.last_name, "last_name")
        ValidatorModels.min_length(user.last_name, "last_name", 3)
        ValidatorModels.max_length(user.last_name, "last_name", 50)
        
        # validaciones de password
        if user.password is not None:
            ValidatorModels.is_password(user.password, "password")
            ValidatorModels.min_length(user.password, "password", 8)
            ValidatorModels.max_length(user.password, "password", 16)
        
        # validaciones de email
        ValidatorModels.not_null(user.email, "email")
        ValidatorModels.not_empty(user.email, "email")
        ValidatorModels.is_email(user.email, "email")
        # validaciones de role
        ValidatorModels.not_null(user.role, "role")
        ValidatorModels.not_empty(user.role, "role")
        

    def validate_id(id : int):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")
        
    
    def validate_user_exists(user):
        if user is None:
            raise CustomError(404, "Usuario no encontrado")
        
    def validate_user_active(is_active):
        if not is_active:
            raise CustomError(401, "El usuario no está activo")
        
    def validate_user_verified(is_verified):
        if not is_verified:
            raise CustomError(401, "El usuario no está verificado")
        

    def validate_credentials(password, hashed_password):
        if not SecurityEncryption().verify_password(password, hashed_password):
            raise CustomError(401, "Credenciales incorrectas")
    