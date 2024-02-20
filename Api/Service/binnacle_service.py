# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Data.binnacle_data import BinnacleData
from Api.Models.binnacle_model import Binnacle


class BinnacleService:
    
    def create_binnacle(binnacle: Binnacle, db: Session):
        try:
            _binnacle = BinnacleData(
                action=binnacle.action,
                error=binnacle.error,
                status_code=binnacle.status_code
            )
            
            db.add(_binnacle)
            db.commit()
            db.refresh(_binnacle)
            return _binnacle
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400, f"Error creating binnacle")
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408, f"Error creating binnacle")
        except Exception as e:
            db.rollback()
            raise CustomError(500, f"Error creating binnacle: {str(e)}")
        
    def get_binnacle(id: int, db: Session):
        try:
            result = db.query(BinnacleData).filter(BinnacleData.id == id).first()
            if result is None:
                raise CustomError(404, "Binnacle not found")
            return result
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error getting binnacle: {str(e)}")
        
    def get_binnacles(db: Session, skip: int = 0, limit: int = 10):
        try:
            result = db.query(BinnacleData).offset(skip).limit(limit).all()
            return result
        except Exception as e:
            raise CustomError(500, f"Error getting binnacles: {str(e)}")
        
    def get_binnacles_by_user_id(user_id: int, db: Session, skip: int = 0, limit: int = 10):
        try:
            result = db.query(BinnacleData).filter(BinnacleData.user_id == user_id).offset(skip).limit(limit).all()
            return result
        except Exception as e:
            raise CustomError(500, f"Error getting binnacles by user id: {str(e)}")
        
    def update_binnacles(binnacle: BinnacleData, db: Session):
        try:
            db.query(BinnacleData).filter(BinnacleData.id == binnacle.id).update(binnacle)
            db.commit()
            return binnacle
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400, f"Error updating binnacle: {str(e)}")
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408, f"Error updating binnacle: {str(e)}")
        except Exception as e:
            db.rollback()
            raise CustomError(500, f"Error updating binnacle: {str(e)}")
        
        
    def delete_binnacle(id: int, db: Session):
        try:
            db.query(BinnacleData).filter(BinnacleData.id == id).delete()
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400, f"Error deleting binnacle: {str(e)}")
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408, f"Error deleting binnacle: {str(e)}")
        except Exception as e:
            db.rollback()
            raise CustomError(500, f"Error deleting binnacle: {str(e)}")

