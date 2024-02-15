# Dependencias
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
#errores
from Core.Validations.custom_error import CustomError
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
# Rutas
from Api.Routes.home_router import home_router
from Api.Routes.user_router import user_router
from Api.Routes.task_router import task_router
from Api.Routes.contact_router import contact_router
from Api.Routes.upload_router import upload_router
from Api.Routes.email_router import email_router
# Base de datos
from Api.Data.conection import ConexionBD

# Cargar variables de entorno
load_dotenv()

# Orígenes permitidos
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

# Configurar la aplicación
app = FastAPI(
  title="Introducción a FastAPI",
  description="Esta es una breve introducción a FastAPI, un framework para construir APIs con Python.",
  version="1.0.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejadores de errores HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {
                "code": exc.status_code, 
                "message": str(exc.detail),
                "url": str(request.url)
            }
        },
    )

# Manejador de errores validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = []
    
    for error in exc.errors():
         errors.append({
            "msg": error["msg"],
            "body": error["loc"][1],
            "input": error["input"]
        })
    
    return JSONResponse(
        status_code=422,
        content={"datails": {
            "code": 422, 
            "message": f"La solicitud no pudo ser procesada",
            }, 
            "errors": errors,
        }
    )
    
# Manejador de errores personalizado
@app.exception_handler(CustomError)
async def unicorn_exception_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.code,
        content={"error": {"code": exc.code, "message": exc.message}},
    )

# Configurar archivos estáticos
resources_path = os.path.join(os.path.dirname(__file__), "Resources/")
uploads_path = os.path.join(os.path.dirname(__file__), "Uploads/")
app.mount("/Resources", StaticFiles(directory=resources_path), name="Resources")
app.mount("/Uploads", StaticFiles(directory=uploads_path), name="Uploads")

# Base de datos
#ConexionBD().verificar_conexion()
ConexionBD().create_tables()
#ConexionBD().drop_tables()


# Rutas de la aplicación
app.include_router(home_router)
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(task_router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(contact_router, prefix="/api/contacts", tags=["Contacts"])
app.include_router(upload_router, prefix="/api/upload", tags=["Upload"])
app.include_router(email_router, prefix="/api/email", tags=["Email"])


