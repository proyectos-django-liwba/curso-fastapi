import asyncio
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from Api.Service.user_service import UserService

async def print_message():
    while True:
        print("Imprimiendo mensaje...")
        await asyncio.sleep(30)
    
async def cleanup_users_not_verified(db: Session):
    try:
        # Calcular la fecha límite para la activación (24 horas atrás)
        # formato de la fecha "yyyy-mm-dd 00:00:00.000000",ejemplo "2024-02-12T19:04:44.876084"
        # pruebas
        #limit_date = datetime.utcnow() - timedelta(seconds=30)
        limit_date = datetime.utcnow() - timedelta(hours=24)
        print(f"Limit date: {limit_date}")
        
        # Obtener usuarios no activados
        inactive_users = UserService.get_user_not_verified(db)
        
        # Eliminar usuarios no activados
        for user in inactive_users:
            print(f"User {user.id} created at: {user.created_at}")
            if user.created_at < limit_date:
                print(f"User {user.id} deleted due to inactivity")
                UserService.delete_user(user.id, db)
            
    except Exception as e:
        print(f"Error cleaning up not verify users: {str(e)}")

async def periodic_cleanup_task(db: Session):
    while True:
        await cleanup_users_not_verified(db)
        # pruebas
        #await asyncio.sleep(30)
        
        # Esperar 24 horas antes de ejecutar la próxima limpieza
        await asyncio.sleep(24 * 60 * 60)

def start_periodic_cleanup(db: Session):
    # prueba de impresión
    #asyncio.create_task(print_message())
    
    # Crear una tarea en segundo plano para la limpieza periódica
    asyncio.create_task(periodic_cleanup_task(db))