from fastapi import APIRouter

# crear un router
middleware_router = APIRouter()


# definir rutas
@middleware_router.get("/")
async def middleware():
    return {"message": "Middleware"}

@middleware_router.get("/get_data_origin")
async def get_data_origin():
    return {"message": "Obteniendo datos de origen"}