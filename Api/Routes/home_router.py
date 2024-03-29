# Dependencias
import os
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


# Crear el router
home_router = APIRouter()

# Definir tag
tag = "Home"

# Configurar archivos de vista
views_path = os.path.join(os.path.dirname(__file__), "../../Views/")
views_path = Jinja2Templates(directory=views_path)

# Definir rutas
@home_router.get("/", tags={tag})
def get_home(request: Request):
  return views_path.TemplateResponse("index.html", {"request": request, "title": "Bienvenido a FastAPI"})