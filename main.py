# Importaciones
import os
# Dependencias
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

#errores
from domain.error import CustomError

# Importar rutas
from router.home_router import home_router
from router.user_router import user_router
from router.task_router import task_router
from router.contact_router import contact_router

# Configurar la aplicación
app = FastAPI(
  title="Introducción a FastAPI",
  description="Esta es una breve introducción a FastAPI, un framework para construir APIs con Python.",
  version="1.0.0",
)

# Manejadores de errores
@app.exception_handler(CustomError)
async def unicorn_exception_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.code,
        content={"error": {"code": exc.code, "message": exc.message}},
    )

# Configurar archivos estáticos
assets_path = os.path.join(os.path.dirname(__file__), "assets/")
app.mount("/assets", StaticFiles(directory=assets_path), name="assets")

# Rutas de la aplicación
app.include_router(home_router)
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(task_router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(contact_router, prefix="/api/contacts", tags=["Contacts"])