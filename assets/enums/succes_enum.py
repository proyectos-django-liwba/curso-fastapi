from enum import Enum

class SuccessType(str, Enum):
    OK = {"code": 200, "message": "OK"}
    CREATED = {"code": 201, "message": "Creado"}
    ACCEPTED = {"code": 202, "message": "Aceptado"}
    NO_CONTENT = {"code": 204, "message": "Sin contenido"}
    RESET_CONTENT = {"code": 205, "message": "Contenido reseteado"}
    PARTIAL_CONTENT = {"code": 206, "message": "Contenido parcial"}
    MULTI_STATUS = {"code": 207, "message": "Multi-estatus"}
    ALREADY_REPORTED = {"code": 208, "message": "Ya reportado"}

