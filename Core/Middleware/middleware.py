from  fastapi import Request
import time
import httpx




async def add_process_time_header(request: Request, call_next):
    #obtener el tiempo de inicio
    start_time = time.time()
    #obtener la respuesta
    response = await call_next(request)
    #calcular el tiempo de procesamiento
    process_time = time.time() - start_time
    #agregar el tiempo de procesamiento a la cabecera
    response.headers["X-Process-Time"] = str(process_time)
    print(process_time)
    return response

async def get_data_origin(request: Request, call_next):
    print("Obteniendo datos de origen...")
    
    # En un entorno local, la dirección IP del cliente es siempre es
    # 127.0.0.1
    client_ip = request.client.host
    print("Cliente IP:", client_ip)

    # Temporalmente, se obtiene la dirección IP de salida en internet
    ip = httpx.get("https://api64.ipify.org").text
    print(ip)
    
    # Solo funciona si tiene una ip publica, no funciona con la local
    res = httpx.get(f"https://ipinfo.io/{ip}")
    print(res.json())
    
    response = await call_next(request)
    return response


async def manager_middleware(request: Request, call_next):
    print(request.url.path)
    
    if request.url.path == "/":
        print("Acceso a la ruta principal")
        return await call_next(request)
    elif request.url.path == "/api/middleware/":
        return await add_process_time_header(request, call_next)
    elif request.url.path == "/api/middleware/get_data_origin":
        return await get_data_origin(request, call_next)

            
    return await call_next(request) 
    
