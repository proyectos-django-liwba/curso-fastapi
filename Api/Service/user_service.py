# Dependencias
from sqlalchemy.orm import Session, load_only
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.user_model import User
from Api.Data.user_data import UserData

class UserService:
        
        def create_user(user: User, db: Session):
            _user = UserData(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                password=user.password,
                role=user.role,
                otp = user.otp
            )
            
            try:
                db.add(_user)
                db.commit()
                db.refresh(_user)
                return _user
            
            except IntegrityError as e:
                db.rollback()
                raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
            except TimeoutError as e:
                db.rollback()
                raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
        
        
        def get_user(id: int, db: Session):
            #result = db.query(UserData).get(id)
            result = db.query(UserData).options(load_only(
                UserData.id,
                UserData.first_name,
                UserData.last_name,
                UserData.email,
                UserData.role
                )).get(id)
        
            if result is None:
                raise CustomError(404, "User not found")
            
            return result
        
        def get_all_users(db: Session):
            return db.query(UserData).all()
        
        def update_user(user: User, db: Session):
        
            _user = db.query(UserData).get(user.id)
    
            if _user is None:
                raise CustomError(404, "User not found")
            
            try: 
                _user.first_name = user.first_name
                _user.last_name = user.last_name
                _user.email = user.email
                _user.password = user.password
                _user.role = user.role
    
                db.commit()
                db.refresh(_user)
    
                return _user
            except IntegrityError as e:
                db.rollback()
                raise CustomError(400,"Data base integrity error", e.orig.diag.message_detail)
            except TimeoutError as e:
                db.rollback()
                raise CustomError(408,"Data base timeout error", e.orig.diag.message_detail)
        
        def delete_user(id: int, db: Session):
            _user = db.query(UserData).get(id)
            
            if _user is None:
                raise CustomError(404, "User not found")
            
            db.delete(_user)
            db.commit()

        def login_user( email: str, password: str ,db: Session):
            user = db.query(User).filter(User.email == email).first()
            ValidatorModels.validate_user_exists(user)
            ValidatorModels.validate_user_verified(user.is_verified)
            ValidatorModels.validate_user_active(user.is_active)
            ValidatorModels.validate_credentials(password, user.password)
            return user

