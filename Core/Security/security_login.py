from fastapi import Request
from datetime import datetime, timedelta
from typing import List
from Core.Validations.custom_error import CustomError


# lista de ips bloqueadas
blacklisted = []

# Función para manejar intentos de login
def handle_login_attempt(request: Request):
    client_ip = request.client.host
    
    #global blacklisted
    # Buscar si el IP ya está en la lista
    for item in blacklisted:
        if item['ip'] == client_ip:
            # Verificar si está bloqueado y si el tiempo de desbloqueo ya pasó
            if item['blocked'] and datetime.now() < item['unblock_time']:
                print("La ip fue bloqueada", item)
                raise CustomError(400, "IP bloqueada temporalmente.", f"Tienes que esperar {item['unblock_time']} para volver a intentar.")
                
            elif item['blocked'] and datetime.now() >= item['unblock_time']:
                # Resetear intentos si el tiempo de bloqueo ha pasado
                item['attempts'] = 1
                item['blocked'] = False
                item['unblock_time'] = None
                #return
                return item
            
            # Si no está bloqueado, aumentar intentos
            item['attempts'] += 1
            print("Nuevo intento de login", item)
            
            # Si los intentos exceden el límite, bloquear
            if item['attempts'] >= 3:
                # Bloquear y establecer tiempo de desbloqueo
                item['blocked'] = True
                item['unblock_time'] = datetime.now() + timedelta(minutes=3)
                print("Intentos de login excedidos", item)
                raise CustomError(400, "IP bloqueada temporalmente.", f"Tienes que esperar {item['unblock_time']} para volver a intentar.")
            
            # Si no exceden el límite, retornar
            #return
            return item

    # Si el IP no está en la lista, agregarlo
    login = {
        'ip': client_ip,
        'attempts': 1,
        'blocked': False,
        'unblock_time': None
    }
    blacklisted.append(login)
    print( "Agregando ip",blacklisted )
    return login
    


def remove_ip_from_blacklist(client_ip: str):
    global blacklisted
    blacklisted = [item for item in blacklisted if item['ip'] != client_ip]
    print("Removiendo ip", blacklisted)