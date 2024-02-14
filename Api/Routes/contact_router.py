# Dependencias
from fastapi import APIRouter, Query, Path, Body
# Importaciones
from Api.Models.contact_model import Contact
from Api.Data.contact_data import contact_list
# Query: Parámetros de consulta, se utiliza para validar y obtener parámetros
# de consulta en una ruta de tipo GET o POST con parámetros de consulta en la URL.

# Crear un router
contact_router = APIRouter()

# Rutas
@contact_router.post("/")
def create_contact(contact: Contact):
    contact_list.append(contact)
    return contact


@contact_router.get("/")
def get_contacts(
    results: int = Query(5, ge=5, le=20, description="Número de resultados")
):
    return contact_list[:results]


@contact_router.get("/by_index")
def get_contact(index: int = Query(0, ge=0, lt=len(contact_list))):
    return contact_list[index]
  
@contact_router.get("/{index}")
def get_contact(index: int = Path(ge=0, lt=len(contact_list))):
    return contact_list[index]


@contact_router.get("/phone")
def get_contact_by_phone(
    phone: str = Query(
        ..., regex=r"^\d{8}$", description="Número de teléfono de 8 dígitos"
    )
):
    result = {}
    for contact in contact_list:
        if contact["phone"] == phone:
            result = contact
            return result

    return result


@contact_router.put("/")
def update_contact(index: int, contact: Contact = Body()):
    contact_list[index] = contact
    return contact


@contact_router.delete("/")
def delete_contact(index: int = Query(0, ge=0, lt=len(contact_list))):
    contact_list.pop(index)
    return contact_list
