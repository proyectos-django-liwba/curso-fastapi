# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Data.tag_data import TagData
from Api.Models.tag_model import Tag

class TagService:
            
        def create_tag(tag: Tag, db: Session ):
    
            _tag = TagData(name=tag.name)
            
            try: 
                db.add(_tag)
                db.commit()
                db.refresh(_tag)
                return _tag
            except IntegrityError as e:
                db.rollback()
                raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
            except TimeoutError as e:
                db.rollback()
                raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
        
        def get_tag(id: int, db: Session):
            result = db.query(TagData).get(id)
        
            if result is None:
                raise CustomError(404, "Tag not found")
            
            return result
        
        def get_all_tags(db: Session):
            return db.query(TagData).order_by(TagData.id).all()
        
        def update_tag( tag: Tag, db: Session):
        
            _tag = db.query(TagData).get(tag.id)
    
            if _tag is None:
                raise CustomError(404, "Tag not found")
            try: 
                _tag.name = tag.name
    
                db.commit()
                db.refresh(_tag)
                return _tag
            except IntegrityError as e:
                db.rollback()
                raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
            except TimeoutError as e:
                db.rollback()
                raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
            
        def delete_tag(id: int, db: Session):
            _tag = db.query(TagData).get(id)
    
            if _tag is None:
                raise CustomError(404, "Tag not found")
 
            db.delete(_tag)
            db.commit()
           