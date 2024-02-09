from fastapi import APIRouter

# Crear el router
user_router = APIRouter()

# Definir rutas
@user_router.get("/{id}")
def get_user(id: int):
  return {"id": id, "name": "John Doe"}