# dependencias
from sqlalchemy.orm import Session
# importaciones
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Api.Service.tag_service import TagService
from Api.Models.tag_model import Tag
from Core.Validations.tag_validation import TagValidation

class TagController:
    
    def create_tag(tag: Tag, db: Session):
        try:
            # validar datos
            TagValidation.validate_create(tag)
            # crear tag
            result = TagService.create_tag(tag, db)
            # retornar respuesta
            return ResponseBase(201, "Tag created", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error creating tag: ",{str(e)})
        
    def get_tag(id: int, db: Session):
        try:
            # validar datos
            TagValidation.validate_id(id)
            # buscar tag
            result = TagService.get_tag(id, db)
            # retornar respuesta
            return ResponseBase(200, "Tag found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error getting tag: ",{str(e)})
        
    
    def get_all_tags(db: Session):
        try:
            # buscar tags
            result = TagService.get_all_tags(db)
            # retornar respuesta
            return ResponseBase(200, "Tags found", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error getting tags: ",{str(e)})
        
    def update_tag(tag: Tag, db: Session):
        try:
            # validar datos
            TagValidation.validate_update(tag)
            # actualizar tag
            result = TagService.update_tag(tag, db)
            # retornar respuesta
            return ResponseBase(200, "Tag updated", result).to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error updating tag: ",{str(e)})
        
    
    def delete_tag(id: int, db: Session):
        try:
            # validar datos
            TagValidation.validate_id(id)
            # eliminar tag
            TagService.delete_tag(id, db)
            # retornar respuesta
            return ResponseBase(200, "Tag deleted").to_dict()
        
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, "Error deleting tag: ",{str(e)})