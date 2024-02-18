from Api.Models.user_model import User
from Core.Validations.validator_models import ValidatorModels

class UserValidation:
    
    def validate_create(user: User):
        # validaciones de nombre
        ValidatorModels.not_empty(user.name, "name")
        ValidatorModels.min_length(user.name, "name", 3)
        ValidatorModels.max_length(user.name, "name", 100)
        # validaciones de last_name
        ValidatorModels.not_empty(user.last_name, "last_name")
        ValidatorModels.min_length(user.last_name, "last_name", 4)
        ValidatorModels.max_length(user.last_name, "last_name", 80)
        # validaciones de email
        ValidatorModels.not_empty(user.email, "email")
        ValidatorModels.min_length(user.email, "email", 10)
        ValidatorModels.max_length(user.email, "email", 50)
        # validaciones de password
        ValidatorModels.not_empty(user.password, "password")
        ValidatorModels.min_length(user.password, "password", 8)
        ValidatorModels.max_length(user.password, "password", 50)

    def validate_update(user):
        # validaciones de nombre
        ValidatorModels.not_empty(user.name, "name")
        ValidatorModels.min_length(user.name, "name", 3)
        ValidatorModels.max_length(user.name, "name", 100)
        # validaciones de last_name
        ValidatorModels.not_empty(user.last_name, "last_name")
        ValidatorModels.min_length(user.last_name, "last_name", 4)
        ValidatorModels.max_length(user.last_name, "last_name", 80)
        # validaciones de email
        ValidatorModels.not_empty(user.email, "email")
        ValidatorModels.min_length(user.email, "email", 10)
        ValidatorModels.max_length(user.email, "email", 50)
        # validaciones de password
        ValidatorModels.not_empty(user.password, "password")
        ValidatorModels.min_length(user.password, "password", 8)
        ValidatorModels.max_length(user.password, "password", 50)
        
    def validate_id(id):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")