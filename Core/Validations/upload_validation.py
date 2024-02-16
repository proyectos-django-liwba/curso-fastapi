from Core.Validations.validator_models import ValidatorModels
from Api.Models.upload_model import Upload


class UploadValidation:

    def validate_create(upload: Upload):
        # validaciones de file
        ValidatorModels.not_null(upload.file, "file")
        ValidatorModels.not_empty(upload.file, "file")
        # validaciones de user
        ValidatorModels.not_null(upload.user_id, "user_id")
        ValidatorModels.is_positive_integer(upload.user_id, "user_id")
        
    def validate_update( upload: Upload):
        # validaciones de file
        ValidatorModels.not_null(upload.file, "file")
        ValidatorModels.not_empty(upload.file, "file")
        
    def validate_id(id):
        # validaciones de id
        ValidatorModels.not_null(id, "id")
        ValidatorModels.is_positive_integer(id, "id")
          
    def validate_file(size, content_type):
        valid_formats = ["image/jpeg", "image/png", "image/jpg"]
        max_size = 1 * 1024 * 1024
        # validar el formato del archivo
        ValidatorModels.valid_formats(content_type, "file", valid_formats)
        # validar el tamaño del archivo
        ValidatorModels.max_size(size, "file", max_size)
        
    def validate_user_id(user_id):
        # validaciones de user_id
        ValidatorModels.not_null(user_id, "user_id")
        ValidatorModels.is_positive_integer(user_id, "user_id")