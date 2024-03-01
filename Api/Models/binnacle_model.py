from pydantic import BaseModel
from typing import Optional

class Binnacle(BaseModel):
    id: Optional[int] = None
    endpoint: str
    method: str
    detail: str
    status_code: int
    user_id: Optional[int] = None
    ip_client: str

    class Config:
        from_attributes = True
        
    def __str__(self):  
        return f"Binnacle(id={self.id}, endpoint={self.endpoint}, method={self.method}, detail={self.detail}, status_code={self.status_code}, user_id={self.user_id}, ip_client={self.ip_client})"