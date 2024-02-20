# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.upload_model import Upload
from Api.Data.upload_data import UploadData

class UploadService:
    
    def create_upload(upload: Upload, db: Session):
        _upload = UploadData(url=upload.url, user_id=upload.user_id)
        
        try: 
            db.add(_upload)
            db.commit()
            db.refresh(_upload)
            return _upload
        
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    
    def get_upload(id: int, db: Session):
        result = db.query(UploadData).get(id)
       
        if result is None:
            raise CustomError(404, "Upload not found")
        
        return result
    
    def get_upload_by_user_id(user_id: int, db: Session):
        return db.query(UploadData).filter(UploadData.user_id == user_id).all()
    
    def update_upload(upload: Upload, db: Session):
      
        _upload = db.query(UploadData).get(upload.id)

        if _upload is None:
            raise CustomError(404, "Upload not found")
        
        try:
            old_url = _upload.url
            _upload.url = upload.url

            db.commit()
            db.refresh(_upload)

            return {
                "upload": _upload,
                "old_url": old_url,
            }
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
    
    
    def delete_upload(id: int, db: Session):
        _upload = db.query(UploadData).get(id)
 
        if _upload is None:
            raise CustomError(404, "Upload not found")
        
        db.delete(_upload)
        db.commit()
        
        return _upload 