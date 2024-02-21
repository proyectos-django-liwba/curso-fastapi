from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from Core.Validations.custom_error import CustomError
import os
class JWT:
    def __init__(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.DEFAULT_EXPIRE_MINUTES = os.getenv("DEFAULT_EXPIRE_MINUTES")

    def create_otp(self, data: dict, token_type: str, expires_minutes: int | None = None):
        to_encode = data.copy()
        expire_minutes = expires_minutes or self.DEFAULT_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        to_encode.update({"exp": expire, "type": token_type})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def create_token(self, data: dict, token_type: str, role: str | None = None, user_id: int | None = None):
        to_encode = data.copy()
        # parsear a int la variable de entorno
        expire_minutes = int(os.getenv("DEFAULT_EXPIRE_MINUTES"))
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)

        # Crear token de acceso
        to_encode.update({"exp": expire, "type": token_type, "role": role, "user_id": user_id})
        access = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return access
    
    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            # Verificar la expiración del token
            
            if "exp" in payload and datetime.utcfromtimestamp(payload["exp"]) < datetime.utcnow():
                raise CustomError(401, "Token expirado")
            
            return payload
        except CustomError as e:
            raise e
        except JWTError as e:
            raise CustomError(401, "Token invalido", e)

        
        