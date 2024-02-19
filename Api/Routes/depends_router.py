from fastapi import APIRouter, Depends, Header
from Core.Validations.custom_error import CustomError

# crear el router
depends_router = APIRouter()


# Dependencias usos
# https://fastapi.tiangolo.com/tutorial/header-params/

# Autenticación
def validate_token(bearer: str = Header()):
    if bearer != "jwt-token": 
        raise CustomError(401, "Unauthorized")
        #raise CustomError(401, "Unauthorized")
    
# Autorización
def validate_admin_user(role: str = Header()):
    if role != "admin":
        raise CustomError(401, "Unauthorized")
    
 # Validación de entrada
def validate_user_id(user_id: int):
    if user_id < 1:
        raise CustomError(400,"El ID del usuario debe ser mayor a 0")
    

# Definir rutas
@depends_router.get("/validate-token", dependencies=[Depends(validate_token)])
def get_users():
    return {"users": "users"}

@depends_router.get("/validate-user-id/{user_id}", dependencies=[Depends(validate_user_id)])
def get_user(user_id: int = Depends(validate_user_id)):
    return {"user_id": user_id}

""" 

def get_current_user(token: str):
# authenticate user
    return User()

@app.get("/items/")
def read_items(user: User = Depends(get_current_user)):
    ...

@app.post("/items/")
def create_item(*, user: User = Depends(get_current_user), item: Item):
    ...

@app.get("/items/{item_id}")
def read_item(*, user: User = Depends(get_current_user), item_id: int):
    ...

@app.delete("/items/{item_id}")
def delete_item(*, user: User = Depends(get_current_user), item_id: int):
    ...

# Simplificación de dependencias
from typing_extensions import Annotated

def get_current_user(token: str):
# authenticate user
    return User()
    
CurrentUser = Annotated[User, Depends(get_current_user)]

@app.get("/items/")
def read_items(user: CurrentUser):
    ...
    
@app.post("/items/")
def create_item(user: CurrentUser, item: Item):
    ...

@app.get("/items/{item_id}")
def read_item(user: CurrentUser, item_id: int):
    ...

@app.delete("/items/{item_id}")
def delete_item(user: CurrentUser, item_id: int):
    ...

"""
