from pydantic import BaseModel
from typing import Optional


class Upload(BaseModel):
    id: Optional[int] = None
    file: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[int] = None
    
    class Config:
        from_attributes = True
        
    def __str__(self):
        return f"Upload(id={self.id}, file={self.file}, url={self.url}, user={self.user_id})"