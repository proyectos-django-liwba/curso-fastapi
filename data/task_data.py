from assets.enums.task_enum import StatusType

# Almacenar tareas
tasks_list = [
    {
        "id": 1,
        "task": "Limpiar la casa",
        "status": StatusType.DONE,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
    {
        "id": 2,
        "task": "Hacer la compra",
        "status": StatusType.PENDING,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
    {
        "id": 3,
        "task": "Cocinar la cena",
        "status": StatusType.PENDING,
        "category": {"id": 1, "name": "Hogar", "description": "Tareas del hogar"},
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Mora Matarrita",
            "email": "correo@correo.com",
        },
    },
]
