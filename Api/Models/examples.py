
# task
task_example_create = {
    "title": "Tarea 1",
    "status": "Pending",
    "category_task_id": 1,
    "user_id": 1,
}

task_example_update = {
    "id": 1,
    "title": "Tarea #",
    "status": "Pending",
    "category_task_id": 1,
    "user_id": 1,
}

# upload
upload_example_create = {
    "file": "base64_file",
    "user_id": 1,
}

upload_example_update = {
    "id": 1,
    "file": "base64_file",
}

# category_task
category_tasks_example_create = {
    "name": "Tarea",
    "description": "Descripción de la tarea"
}

category_tasks_example_update = {
    "id": 1,
    "name": "Tarea",
    "description": "Descripción de la tarea"
}

# user
user_example_create = {
    "first_name": "Wilfredo",
    "last_name": "Barquero Herrera",
    "email": "correo@correo.com",
    "password": "Usuario1234"
}

user_example_update = {
    "id": 1,
    "first_name": "Wilfredo",
    "last_name": "Barquero Herrera",
    "email": "correo@correo.com"
}

user_example_change_password = {
    "id": 1,
    "password": "Usuario1234",
    "new_password": "Usuario2345"
}
user_example_login = {
    "email": "correo@correo.com",
    "password": "Usuario1234"
}

user_active_example = {
    "otp": "token",
}

# tag

tag_example_create = {
    "name": "Tag 1"
}

tag_example_update = {
    "id": 1,
    "name": "Tag 1"
}