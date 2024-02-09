from pydantic import BaseModel

class User(BaseModel):
  id: int
  first_name: str
  last_name: str
  email: str
  