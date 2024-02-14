from enum import Enum

class ErrorType(str, Enum):
    NOT_FOUND = {"code": 404, "message": "Recurso no encontrado"}
    BAD_REQUEST = {"code": 400, "message": "Solicitud incorrecta"}
    UNAUTHORIZED = {"code": 401, "message": "No autorizado"}
    FORBIDDEN = {"code": 403, "message": "Prohibido"}
    INTERNAL_SERVER_ERROR = {"code": 500, "message": "Error interno del servidor"}
