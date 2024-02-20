# Dependencias
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
# Importaciones
from Api.Data.conection import ConexionBD
from Api.Controllers.tag_controller import TagController
from Api.Models.tag_model import Tag
from Api.Models.examples import tag_example_create, tag_example_update

# Crear router
tag_router = APIRouter()

# definir rutas
@tag_router.post("/")
def create_tag(tag: Tag = Body(example=tag_example_create), db: Session = Depends(ConexionBD().get_db)):
    return TagController.create_tag(tag, db)

@tag_router.get("/{tag_id}")
def get_tag(tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TagController.get_tag(tag_id, db)

@tag_router.get("/")
def get_all_tags(db: Session = Depends(ConexionBD().get_db)):
    return TagController.get_all_tags(db)

@tag_router.put("/")
def update_tag(tag: Tag = Body(example=tag_example_update), db: Session = Depends(ConexionBD().get_db)):
    return TagController.update_tag(tag, db)

@tag_router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(ConexionBD().get_db)):
    return TagController.delete_tag(tag_id, db)
