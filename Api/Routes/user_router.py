# dependencias
from fastapi import APIRouter, Depends, Body, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import text
from passlib.context import CryptContext
# importaciones
from Api.Controllers.user_controller import UserController
from Api.Data.conection import ConexionBD
from Api.Models.user_model import User
from Api.Models.examples import user_example_create, user_example_update, user_example_login,user_example_change_password,user_active_example


# Crear el router
user_router = APIRouter()

# Definir rutas
@user_router.post("/")
async def create_user(background_tasks: BackgroundTasks, user: User = Body(example=user_example_create), db: Session = Depends(ConexionBD().get_db)):
    return await UserController.create_user(user, db, background_tasks)
@user_router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UserController.get_user(user_id, db)

@user_router.get("/")
async def get_all_users(db: Session = Depends(ConexionBD().get_db)):
    return UserController.get_all_users(db)

@user_router.put("/")
async def update_user(user: User = Body(example=user_example_update), db: Session = Depends(ConexionBD().get_db)):
    return UserController.update_user(user, db)

@user_router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UserController.delete_user(user_id, db)

@user_router.post("/login")
async def login_user(user: User = Body(example=user_example_login), db: Session = Depends(ConexionBD().get_db)):
    return UserController.login_user(user, db)

@user_router.patch("/change_password")
async def change_password(id, password, new_password, confirm_password, db: Session = Depends(ConexionBD().get_db)):
    return UserController.change_password(id, password, new_password,confirm_password, db)

@user_router.post("/activate_account")
async def activate_account(user: User = Body(example=user_active_example), db: Session = Depends(ConexionBD().get_db)):
    return UserController.activate_account(user, db)

@user_router.post("/verify_account")
async def verify_account(user: User = Body(example=user_active_example), db: Session = Depends(ConexionBD().get_db)):
    
    return UserController.verify_account(user, db)

@user_router.post("/get_user_not_verified")
async def get_user_not_verified(db: Session = Depends(ConexionBD().get_db)):
    return UserController.get_user_not_verified(db)

@user_router.post("/forgot_password")
async def forgot_password(background_tasks: BackgroundTasks,email, db: Session = Depends(ConexionBD().get_db)):
    return UserController.forgot_password(email, db, background_tasks)

@user_router.post("/desactivate_account/{user_id}")
async def desactivate_account(user_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UserController.desactivate_account(user_id, db)

@user_router.patch("/reset_password")
async def reset_password(otp, password,conform_password, db: Session = Depends(ConexionBD().get_db)):
    return UserController.reset_password(otp, password,conform_password, db)

# Consultas sin ORM
""" 
@user_router.get("/by_sql")
async def get_users(db: Session = Depends(ConexionBD().get_db)):
    try:
        # Ejecutar la consulta sql
        result = db.execute(
            text("SELECT id, username, first_name, last_name, email, role from users")
        )

        users = []
        for row in result:
            user_data = {
                "id": row[0],
                "username": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "email": row[4],
                "role": row[5],
            }
            users.append(user_data)

        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")

@user_router.get("/by_bd_function")
async def get_users(db: Session = Depends(ConexionBD().get_db)):
    try:
        # Ejecutar la consulta sql
        result = db.execute(
            text("SELECT * FROM obtener_usuarios();")
        )

        users = []
        for row in result:
            user_data = {
                "id": row[0],
                "username": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "email": row[4],
                "role": row[5],
            }
            users.append(user_data)

        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")


@user_router.get("/by_orm")
async def get_user(db: Session = Depends(ConexionBD().get_db)):
    try:

        users = db.query(UserSchema).all()
        return {"users": users}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}")

@user_router.get("/by_id/{user_id}")
async def get_user(user_id: int ,db: Session = Depends(ConexionBD().get_db)):
    try:
        
        if user_id is None:
            raise CustomError(400, "El id del usuario es requerido")
        
        if user_id <= 0:
            raise CustomError(400, "El id del usuario debe ser mayor a 0")
        
        user = db.query(UserSchema).filter(UserSchema.id == user_id).first()

        if user is None:
            raise CustomError(404, "Usuario no encontrado")
       
        return {"user": user}

    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al obtener los usuarios: {str(e)}") """
