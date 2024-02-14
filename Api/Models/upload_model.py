from pydantic import BaseModel

class Upload(BaseModel):
    first_name: int
    last_name: str
    email: str
    image: str
    