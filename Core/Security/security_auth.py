from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
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

    def create_token(self, data: dict, token_type: str, expires_minutes: int | None = None, role: str | None = None, user_id: int | None = None):
        to_encode = data.copy()
        expire_minutes = expires_minutes or self.DEFAULT_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        refresh_expire = datetime.now(timezone.utc) + timedelta(days=3)
        refresh_encode = to_encode.update({"exp": refresh_expire, "type": token_type, "role": role, "user_id": user_id})
        to_encode.update({"exp": expire, "type": token_type, "role": role, "user_id": user_id})
        access = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        refresh = jwt.encode(refresh_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return {"access": access, "refresh": refresh}
    
    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError:
            return None
        
        