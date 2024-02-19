from Core.Validations.validator_models import ValidatorModels
from Api.Models.tag_model import Tag

class TagValidation:
    
    def validate_create(tag: Tag):
        # validaciones de name
        ValidatorModels.not_empty(tag.name, "name")
        ValidatorModels.min_length(tag.name, "name", 4)
        ValidatorModels.max_length(tag.name, "name", 100)
    
    def validate_update(tag: Tag):
        # validaciones de id
        ValidatorModels.not_null(tag.id, "id")
        ValidatorModels.is_positive_integer(tag.id, "id")
        # validaciones de name
        ValidatorModels.not_empty(tag.name, "name")
        ValidatorModels.min_length(tag.name, "name", 4)
        ValidatorModels.max_length(tag.name, "name", 100)
     
    def validate_id(id: int):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")