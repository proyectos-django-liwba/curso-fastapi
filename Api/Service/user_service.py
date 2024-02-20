# Dependencias
from sqlalchemy.orm import Session, load_only
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.user_model import User
from Api.Data.user_data import UserData
from Core.Validations.user_validation import UserValidation

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

    def login_user(email: str, password: str, db: Session):
        user = db.query(UserData).filter(UserData.email == email).first()
        UserValidation.validate_user_exists(user)
        UserValidation.validate_user_verified(user.is_verified)
        UserValidation.validate_user_active(user.is_active)
        UserValidation.validate_credentials(password, user.password)

        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role
        }
        return user_data
    
    def change_password(id, password, new_password, db: Session):
        user = db.query(UserData).get(id)
        UserValidation.validate_user_exists(user)
        UserValidation.validate_user_verified(user.is_verified)
        UserValidation.validate_user_active(user.is_active)
        UserValidation.validate_credentials(password, user.password)
        user.password = new_password
        db.commit()
        db.refresh(user)
        return user
    
    def activate_user(otp, db: Session):
        user = db.query(UserData).filter(UserData.otp == otp).first()
        UserValidation.validate_user_exists(user)
        user.is_active = True
        user.otp = None
        db.commit()
        db.refresh(user)
        return user
    
    def verify_user(otp, db: Session):
        #obtener usuario por otp
        user = db.query(UserData).filter(UserData.otp == otp).first()
        UserValidation.validate_user_exists(user)
        user.is_verified = True
        user.otp = None
        db.commit()
        db.refresh(user)
        return user
    
    def get_user_not_verified(db: Session):
        return db.query(UserData).filter(UserData.is_verified == False).all()
    
    def forgot_password(email, otp, db: Session):
        user = db.query(UserData).filter(UserData.email == email).first()
        UserValidation.validate_user_exists(user)
        UserValidation.validate_user_verified(user.is_verified)
        UserValidation.validate_user_active(user.is_active)
        user.otp = otp
        db.commit()
        db.refresh(user)
        return user