from passlib.context import CryptContext
class SecurityEncryption:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_password(password: str) -> str:
        return SecurityEncryption.pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return SecurityEncryption.pwd_context.verify(plain_password, hashed_password)