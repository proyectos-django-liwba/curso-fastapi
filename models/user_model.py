from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(..., min_length=4, max_length=30)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=11, max_length=50)
    password: str = Field(..., min_length=8, max_length=16)
    role: str = Field("user", min_length=4, max_length=5)
    

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "WilfredoBH",
                "first_name": "Wilfredo",
                "last_name": "Barquero Herrera",
                "email": "liwbarqueroh@gmail.com",
                "password": "usuario1234",
                "role": "user",
            }
        }
        

