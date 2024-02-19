from pydantic import BaseModel
from typing import Optional

class Session(BaseModel):
    id: Optional[int] = None
    user_id: int
    token: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True