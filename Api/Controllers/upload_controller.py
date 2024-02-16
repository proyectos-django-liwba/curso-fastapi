# Dependencias
import os
from uuid import uuid4
from typing import List
from sqlalchemy.orm import Session

# Importaciones
from Api.Response.response_base import ResponseBase
from Core.Validations.custom_error import CustomError
from Api.Models.upload_model import Upload
from Api.Service.upload_Service import UploadService
from Core.Validations.upload_validation import UploadValidation
from Core.Files.file import FileManager

class UploadController:
    
    def create_upload(upload: Upload, db: Session):
        try:
            # validación de datos
            UploadValidation.validate_create(upload)
            
            # convertir la imagen a bytes
            image = FileManager.convert_base64_to_image(upload.file)
            # obtener información del archivo
            type_image = FileManager.get_type_image(upload.file)
            content_type = FileManager.get_content_type(upload.file)
            size_image = len(image)
            
            # validar el archivo
            UploadValidation.validate_file(size_image, content_type)

            # generar nombre unico para el archivo
            file_name = f"{uuid4()}.{type_image}"

            # guardar el archivo en la carpeta Uploads
            file_path = os.path.join("Uploads", file_name)    
            FileManager.save_image(image, file_path)
            upload.url = f"http://localhost:8000/Uploads/{file_name}"
            
            # guardar el archivo en la base de datos
            result = UploadService.create_upload(upload, db)
            
            # Retornar la respuesta
            return ResponseBase(201, "Upload created successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al crear el archivo: {str(e)}")
        
    def get_upload(upload_id: int, db: Session):
        try:
            # validación de datos
            UploadValidation.validate_id(upload_id)

            result = UploadService.get_upload(upload_id, db)
            return ResponseBase(200, "Upload obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al obtener el archivo: {str(e)}")
    
    def get_upload_by_user_id(user_id: int, db: Session):
        try:
            # validar id
            UploadValidation.validate_user_id(user_id)
            
            result = UploadService.get_upload_by_user_id(user_id, db)
            return ResponseBase(200, "Upload obtained successfully", result).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al obtener el archivo: {str(e)}")

    def update_upload( upload: Upload, db: Session):
        try:
            # validación de datos
            UploadValidation.validate_update(upload)
            
            # convertir la imagen a bytes
            image = FileManager.convert_base64_to_image(upload.file)
            # obtener información del archivo
            type_image = FileManager.get_type_image(upload.file)
            content_type = FileManager.get_content_type(upload.file)
            size_image = len(image)
            
            # validar el archivo
            UploadValidation.validate_file(size_image, content_type)
            
            # generar nombre unico para el archivo
            file_name = f"{uuid4()}.{type_image}"

            # guardar el archivo en la carpeta Uploads
            file_path = os.path.join("Uploads", file_name)    
            FileManager.save_image(image, file_path)
            upload.url = f"http://localhost:8000/Uploads/{file_name}"
            
            # actualizar el archivo en la base de datos
            result = UploadService.update_upload(upload, db)
            
            # eliminar el archivo anterior
            FileManager.delete_file(result["old_url"])
            
            return ResponseBase(200, "Upload updated successfully", result["upload"]).to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al actualizar el archivo: {str(e)}")
    
    def delete_upload(upload_id: int, db: Session):
        try:
            # validar id
            UploadValidation.validate_id(upload_id)
            
            result = UploadService.delete_upload(upload_id, db)
            
            if result:
                # eliminar el archivo de la carpeta Uploads
                FileManager.delete_file(result.url)
                
            return ResponseBase(200, "Upload deleted successfully").to_dict()
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al eliminar el archivo: {str(e)}")
    
    