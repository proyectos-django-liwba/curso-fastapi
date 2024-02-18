from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str 
    password: Optional[str] = None 
    role: Optional[str] = "user"  
    otp: Optional[str] = None
    
    class Config:
        from_attributes = True
 
    def __str__(self):
        return f"User: ( id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, role={self.role}, otp={self.otp}, password={self.password} )"
