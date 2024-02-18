from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=4, max_length=30)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=11, max_length=50)
    password: str = Field(..., min_length=8, max_length=16)
    role: str = Field("user", min_length=4, max_length=5)
    image: Optional[str] = None
    birthdate: Optional[str] = None
    term_conditions: Optional[bool] = False
    is_verified: Optional[bool] = False 
    last_login: Optional[str] = None
    is_active: Optional[bool] = True
    phone: Optional[int] = None
    otp: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "WilfredoBH",
                "first_name": "Wilfredo",
                "last_name": "Barquero Herrera",
                "email": "elmermejias47@gmail.com",
                "password": "usuario1234",
                "role": "user",
                "phone": 12345678,
            }
        }
        