# Guía de FastAPI 2024 
[![FastAPI](./Resources/Images/fastapi.png)](https://fastapi.tiangolo.com/)


## Desarrolladores 
![coders](./Resources/Images/coders.png)

* 🧑‍💻Wilfredo Barquero Herrera

    - [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](liwbarqueroh@gmail.com )

    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/liwBh)

    - [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wilfredo-barquero-herrera-17bb29258)


* 👨‍💻Elmer Mejias Carranza

    - [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://elmermejias47@gmail.com)

    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ing-Elmer)

    - [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ermer-mejias-carranza-a36b39232)

## Arquitectura de proyecto

##### 1. Descripción de las capas:
* 📦**Views**: vistas de la api
* 📦**Uploads**: Almacenamiento de archivos 
* 📦**Api**: 
    - 📁**Router**: implementación de rutas para cada modulo
        ```
            file_router.py
        ```
    - 📁**Models**: Modelos Pydantic, para validaciones de request
        ```
            file_model.py
        ```
    - 📁**Data**: Capa de base de datos contiene la configuración y schema models "tablas"
        ```
            connection_data.py
            file_data.py
        ```
    - 📁**Controller**: Capa intermedia que abstrae la lógica de las rutas, se concentra en realizar los llamados de otras capas y validaciones.
        ```
            file_controller.py
        ``` 
    - 📁**Service**: Capa intermedia que abstrae la lógica de la base de datos
        ```
            file_service.py
        ```
* 📦**Core**: Lógica principal del proyecto
    - 📁**Validations**: validaciones - enums
        ```
            file_validation.py
        ``` 
    - 📁**File**: manejo de archivos
        ```
            file_file.py
        ``` 
    - 📁**Email**: manejo de emails 
        ```
            file_email.py
        ``` 
    - 📁**Security**: lógica de seguridad como permisos, autenticación, encriptaron; 
    ```
        security_permissions.py
        security_auth.py
        security_encryption.py
    ```  
* 📦**Resources**: Acceso a recursos internos de proyecto: 
    - 📁**Template**: código html que se inyecte en lógica
    - 📁**Images**: imágenes de vistas y templates
    - 📁**Styles**: estilos css, scss, etc...
    - 📁**Js**: código javascript para template y vistas
* [⚙️**main.py**](main.py): archivo principal de ejecución del proyecto,configuración y implementación de rutas

##### 2. Estructura de carpetas:
```
app/
├── core/
│   └──validations/
│       └── file_validation.py
│       └── ...
│   └──file/
│       └── file_file.py
│       └── ...
│   └──emails/
│       └── file_email.py
│       └── ...
│   └──security/
│       └── permissions_security.py
│       └── auth_security.py
│       └── encryption_security.py
│       └── ...
│
│
├── uploads/
│
│
├── views/
│
├── resources/ 
│   └── template   
│       └── file.html
│       └── ...
│   └── images/   
│       └── file.png
│       └── file.jpg
│       └── file.web
│       └── file.jpeg
│       └── ...
│   └── styles/   
│       └── file.css
│       └── file.scss
│       └── ...
│   └── js/   
│       └── file.js
│       └── ...
├── api/            
│   └── routers/   
│       └── file_router.py
│       └── ...
│   └── models/      
│       └── file_model.py
│       └── ...
│   └── data/   
│       └── connection_data.py
│       └── file_data.py
│       └── ...
│   └── controller/      
│       └── file_controller.py
│       └── ...
└── main.py

```

## Contenido de la guía 📖
* [Desarrolladores](#desarrolladores)
* [0. Arquitectura de proyecto](#arquitectura-de-proyecto)
    - [1.Descripción de las capas](#1-descripción-de-las-capas)
    - [2. Estructura de carpetas](#2-estructura-de-carpetas)
* [1. FastAPI](#1-fastapi)
* [2. Iniciar proyecto](#2-iniciar-proyecto)
    - [Crear proyecto](#21-crear-proyecto)
    - [Crear servidor](#22-crear-servidor)
    - [Comandos servidor](#23-comandos-de-inicio-servidor)
* [3. Instalación de dependencias](#3-instalación-de-dependencias)
    - [Jinga2](#31-manejo-de-archivos-jinja2)
    - [SqlAlchemy](#32-orm---sql-sqlalchemy)
    - [Pydantic](#33-validación-pydantic)
    - [Python Dotenv](#34-Variables-de-entorno---Python-Dotenv)
    - [Python Multipart](#35-manejo-de-archivos---python-multipart)
    - [Fastapi Mail](#36-envio-de-correos---fastapi-mail)
    - [Passlib](#37-hasheo-de-contraseña-passlib)
    - [Alembic](#38-migraciones-alembic)
    - [Email Validator](#39-validación-de-correo---email-validator)
    - [Json Web Token](#310-Autentificación-JWT)
    - [WebSocket](#311-Websocket)
    - [HTTPX](#312-HTTPX)
* [4. Base de datos](#4-base-de-datos)
    - [Conector Postgre](#411-conector-bd-postgre-sql)
    - [Conector Mysql](#412-conector-bd-mysql)
* [5. Migraciones](#5-migraciones)
    - [Iniciar proyecto](#51-configuración-alembic)
    - [Iniciar proyecto](#52-comandos-alembic)
* [6. Auth JWT](#6-auth-jwt)
* [7. Permisos](#7-permisos)
* [8. Bitácora](#8-bitacora)
* [9. Dependencias](#9-dependencias)
* [10. Middleware](#10-middleware)
* [11. Anotaciones](#11-anotaciones)
* [12. Tareas en segundo plano](#12-tareas-en-segundo-plano)
* [13. Socket](#13-socket)
* [14. Estáticos](#14-estaticos)
* [15. Template](#15-template)
* [16. Mail](#16-mail)
* [17. Manejo de archivos](#17-manejo-de-archivos)
* [18. Manejo de errores](#18-manejo-de-errores)
* [19. Encriptado de datos](#19-encriptado-de-datos)
* [20. Flujo de trabajo de módulos](#20-flujo-de-trabajo-de-módulos)
* [21. Descripción función de packages](#21-descripción-función-de-packages)
* [22. Relaciones en ORM - Alchemist](#22-relaciones-en-orm---alchemist)
* [23. Variables de entorno](#23-variables-de-entorno)
* [24. Notación de ellipsis](#24-notación-de-ellipsis)
* [25. Lista de errores HTTP](#25-lista-de-errores-http)
* [26. Problemas con rutas](#26-problemas-con-rutas)
* [27. Problemas con el Interprete](#27-problemas-con-el-interprete)
* [28. Problemas con alembic](#28-problemas-con-alembic)

## 1. FastAPI 
* [Documentación oficial](https://fastapi.tiangolo.com/)

## 2. Iniciar proyecto

#### 2.1 crear proyecto
* Crear carpeta raíz

* Crear entorno virtual: 
```
python -m venv ./env/env1
```

* Activar env linux: 
```
source env/env1/bin/activate
```

* Activar env windows: 
```
./env/env1/Scripts/activate
```

* [Documentación venv](https://docs.python.org/es/3/library/venv.html)
* Revisar librerías instaladas: 
```
pip list
```
```
pip freeze
```

* Revisar version de python: 
```
python -V
```

* Actualizar pip si se requiere: 
```
python.exe -m pip install --upgrade pip
```

#### 2.2 Crear servidor
* Crear archivo main.py
* Instalar FastAPI:
```
 pip install fastapi
 ```
* Instalar sevidor = Uvicorn: 
```
pip install uvicorn
```
* Instalar dependencias: 
```
pip install -r requirements.txt
```
* Crear archivo requirements.txt: 
```
pip freeze > requirements.txt
```
* Revisar dependencias: 
``` 
pip freeze
```

#### 2.3 Comandos de inicio servidor
* Iniciar servidor con auto recarga: 
```
uvicorn main:app --reload
```

* Iniciar servidor con puerto: 
```
uvicorn main:app --reload --port 8000
```

* Iniciar servidor con nombre y host: 
```
uvicorn main:app --reload --port 8000 --host 0.0.0.0
```

## 3. Instalación de dependencias

#### 3.1 Manejo de archivos: Jinja2
* Instalar dependencia: 
```
pip install jinja2
```
* Descripción: Jinja2 es un motor de plantillas para Python. Es rápido, ampliamente utilizado y seguro.
* [Documentación jinja2](https://pypi.org/project/Jinja2/)

#### 3.2 ORM - SQL: SQLAlchemy
* Instalar dependencia: `pip install sqlalchemy`
* Descripción: SQLAlchemy es un kit de herramientas SQL para Python.
* [Documentación SQLAlchemy](https://www.sqlalchemy.org/)
* [Documentación Instalación](https://docs.sqlalchemy.org/en/20/intro.html#installation)
* [Documentación Guía](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)


#### 3.3 Validación Pydantic
* Instalar dependencia: 
```
pip install pydantic
```
* Descripción: Pydantic es una librería para validar datos en Python.

* [Documentación Validaciones](https://docs.pydantic.dev/latest/concepts/validators/) 

* [Documentación Tipos de datos](https://docs.pydantic.dev/1.10/usage/types/#pydantic-types)

* Instalar validación de email: 
```
pip install pydantic[email]
```

#### 3.4 Variables de entorno - Python Dotenv
* Instalar dependencia: 
```
pip install python-dotenv
```
* Descripción: python-dotenv lee variables de entorno desde archivos .env.

* [Documentación python-dotenv](https://pypi.org/project/python-dotenv/)

#### 3.5 Manejo de archivos - Python Multipart
* Instalar dependencia: 
```
pip install python-multipart
```

* Descripción: python-multipart es una librería para manejar datos multipart en Python.
* [Documentación python-multipart](https://pypi.org/project/python-multipart/)
* [Documentación Uploadfile](https://fastapi.tiangolo.com/reference/uploadfile/)

#### 3.6 Envio de correos - Fastapi Mail
* Instalar dependencia: 
```
pip install fastapi-mail
```
* Descripción: es una librería para el envió de correos
* [Documentación fastapi-mail](https://sabuhish.github.io/fastapi-mail/example/)

#### 3.7  Hasheo de contraseña Passlib
* Instalar dependencia: ```pip install passlib[bcrypt]```
* [Docuementación passlib](https://passlib.readthedocs.io/en/stable/)
* [Docuementación Guía](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-passlib)

#### 3.8  Migraciones Alembic
* Configurar las variables de entorno en un archivo .env
    ```* Instalar dependencia:```pip install alembic ```
* [Documentación alembic](https://alembic.sqlalchemy.org/en/latest/)

#### 3.9 Validación de correo - Email validator
* Instalar dependencia 
```
pip install email-validator
```
* [Documentación Email Validator](https://pypi.org/project/email-validator/)

#### 3.10 Autentificación JWT
* Instalar dependencia 
```
pip install "python-jose[cryptography]"
```
* [Documentación](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

#### 3.11 Websocket
* Instalar dependencia: 
```
pip install websockets
 ```
 * [Documentación](https://fastapi.tiangolo.com/advanced/websockets/)

#### 3.12 HTTPX
* Instalar dependencia: 
```
pip install httpx
 ```
 * [Documentación](https://www.python-httpx.org/)

## 4. Base de datos
* Cada base de datos requiere un conector que se debe instalar de forma independiente. Luego configurar la conexión con esa base de datos.


#### 4.1.1 Conector BD Postgre SQL
* Instalar dependencia: 
```
pip install psycopg2
 ```
* [Documentación](https://www.psycopg.org/docs/install.html#quick-install)

#### 4.1.2 Conector BD MySQL
* Instalar dependencia: 
```
pip install mysql-conector-python
 ```
 * [Documentación Conector](https://dev.mysql.com/doc/connector-python/en/)
 * [Documentación Guía](https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html)


## 5. Migraciones 

#### 5.1 configuración Alembic
* ⚠️La base de datos debe estar limpia, sin tablas
* Iniciar Alembic en el proyecto: ```alembic init alembic```
* Ubicación de migraciones generadas: alembic/versions/
* Configurar archivo env.py 
    - 1: importar mis modelos
        ```
            # schema models
            from data.user_schema import UserSchema
            from data.category_task_schema import CategoryTaskSchema
        ```
    - 2: Agregar url de conexión a base de datos
        ```
            config = context.config
            config.set_main_option('sqlalchemy.url',"driver://user:pass@localhost/dbname")
        ```
    - 3: Agregar los shemas de los modelos a alembic
        ```
            target_metadata = {schemaModel1.metadata, schemaModel2.metadata}
        ```
* Configurar archivo alembic.ini, agregando la url de conexión a bd
```sqlalchemy.url = driver://user:pass@localhost/dbname```

#### 5.2 Comandos Alembic
* Crear migración: ```alembic revision --autogenerate -m "nombre-migracion"```
* Aplicar la ultima migración: ```alembic upgrade head```

## 6. Auth JWT

* Configurar variables de entorno 
 ```
SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
DEFAULT_EXPIRE_MINUTES = 30
```
* Guia de uso
    - 1: Importación
    ```
    from datetime import datetime, timedelta, timezone
    from jose import JWTError, jwt
    import os
    ```
    - 2: Crear constructor
    ```
    def __init__(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.DEFAULT_EXPIRE_MINUTES = os.getenv("DEFAULT_EXPIRE_MINUTES")
    ```
    - 3: Crear el metodo para generar tokens
    ```
        def create_token(self, data: dict, token_type: str, expires_minutes: int | None = None):
        to_encode = data.copy()
        expire_minutes = expires_minutes or self.DEFAULT_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        to_encode.update({"exp": expire, "type": token_type})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    ```

## 7. Permisos
* Guia de uso
    - 1: Importación
    ```
    from Core.Security.security_auth import JWT
    from Api.Service.user_service import UserService
    from Core.Validations.custom_error import CustomError
    from Core.Validations.user_validation import UserValidation
    from Api.Data.conection import ConexionBD
    from sqlalchemy.orm import Session
    from typing import List
    ```
    - 2: Crear El metodo para verificar el rol
    ```
    def verify_role(token: str, role: List, db: Session) -> dict:
        # verificar token
        jwt = JWT()
        data_token =  jwt.verify_token(token)
        
        # verificar rol en bd
        user = UserService.get_user(data_token["user_id"], db)

        # validaciones de usuario
        
        UserValidation.validate_user_exists(user)
        UserValidation.validate_user_verified(user)
        UserValidation.validate_user_active(user)
        
        if len(role) == 0:
            raise CustomError(500, "No se ha especificado un rol para verificar permisos")
        
        available = False
        for rol in role:
            if user.role == rol and data_token["role"] == rol:
                available = True
                break
            
        if not available:
            raise CustomError(403, "No tienes permisos para realizar esta acción")
        
        return {
            "user": user,
            "token": token,
        }
        
    ```
    - 3 En el archivo de depends_router.py
    * Validar la autentificación del usuario metiante el token de JWT
    ```
    def validate_token(bearer: str = Header()):
        if bearer != "jwt-token": 
            raise CustomError(401, "Unauthorized")
    ```
    
    * Validar permisos de Administrador
    ```
    def validate_admin_user(role: str = Header()):
        if role != "admin":
            raise CustomError(401, "Unauthorized")
    ```
    ```
    def validate_auth_admin( bearer: str = Header(), db: Session = Depends(ConexionBD().get_db)):
        return Permission.verify_role(bearer, ["admin"], db)
    ```

    * Validar permisos de usuario
    ```
    def validate_auth_user( bearer: str = Header(),db: Session = Depends(ConexionBD().get_db)):
        return Permission.verify_role(bearer, ["user"], db)
    ```

    * Crear los Enpoinds de prueba 
    ```
    @depends_router.get("/only_user", dependencies=[Depends(validate_auth_user)])
    def get_user_auth(user_data: dict = Depends(validate_auth_user)):
        
        user = user_data["user"]
        token = user_data["token"]
        print(token)

        return {"user": user}

    @depends_router.get("/only_admin", dependencies=[Depends(validate_auth_admin)])
    def get_admin_auth(user_data: dict = Depends(validate_auth_admin)):
        
        user = user_data["user"]
        token = user_data["token"]
        print(token)

        return {"admin": user}
    ```

## 8. Bitacora
Crear una bitácora en una aplicación, ya sea en FastAPI u otro framework, es una práctica importante por varias razones:

* Depuración y diagnóstico de errores: puede ayudar a identificar problemas y errores en la aplicación al registrar eventos relevantes, como excepciones, errores de validación, tiempos de respuesta, etc. 

* Seguridad: Los registros pueden ayudar a detectar intentos de intrusión o actividades sospechosas en la aplicación. Registrar eventos como intentos de inicio de sesión fallidos, solicitudes de recursos no autorizados, etc., puede ayudar a identificar y mitigar posibles amenazas de seguridad.

* Auditoría y seguimiento: Mantener un registro de todas las actividades realizadas en la aplicación puede ser crucial para la auditoría y el seguimiento. Por ejemplo, en una aplicación financiera, registrar cada transacción realizada podría ser necesario para cumplir con los requisitos regulatorios.

* Crear un modelo este paso es opcional con datos de interés para registrar
```
from pydantic import BaseModel
from typing import Optional

class Binnacle(BaseModel):
    id: Optional[int] = None
    endpoint: str
    method: str
    detail: str
    status_code: int
    user_id: Optional[int] = None
    ip_client: str

    class Config:
        orm_mode = True
        
    def __str__(self):  
        return f"Binnacle(id={self.id}, endpoint={self.endpoint}, method={self.method}, detail={self.detail}, status_code={self.status_code}, user_id={self.user_id}, ip_client={self.ip_client})"
```
* Crear un modelo schema o data para la tabla
```
from sqlalchemy import Column,ForeignKey, BigInteger,Integer, String, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD


class BinnacleData(ConexionBD.Base): 
    __tablename__ = "binnacles"
    
    id = Column(BigInteger, primary_key=True, index=True)
    endpoint = Column(String(100))
    method = Column(String(100))
    detail = Column(String(300))
    status_code = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    ip_client = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    
    def __str__(self):
        return f"BinnacleData(id={self.id}, endpoint={self.endpoint}, method={self.method}, detail={self.detail}, status_code={self.status_code}, user_id={self.user_id}, ip_client={self.ip_client}, created_at={self.created_at})"
    
```
* Crear un service para el manejo de las operaciones en base de datos 
```
# Dependencias
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, TimeoutError
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Data.binnacle_data import BinnacleData
from Api.Models.binnacle_model import Binnacle


class BinnacleService:
    
    def create_binnacle(binnacle: Binnacle, db: Session):
        try:
            _binnacle = BinnacleData(
                endpoint=binnacle.endpoint,
                method=binnacle.method,
                detail=binnacle.detail,
                status_code=binnacle.status_code,
                user_id=binnacle.user_id,
                ip_client=binnacle.ip_client
            )
            
            db.add(_binnacle)
            db.commit()
            db.refresh(_binnacle)
            return _binnacle
        except IntegrityError as e:
            db.rollback()
            raise CustomError(400, "Error creating binnacle", e.orig.diag.message_detail)
        except TimeoutError as e:
            db.rollback()
            raise CustomError(408, "Error creating binnacle", e.orig.diag.message_detail)
        except Exception as e:
            db.rollback()
            raise CustomError(500, "Error creating binnacle", str(e))
```
* Implementar la creación de registros cuando ocurren excepciones
```
# Bitácora
from Api.Models.binnacle_model import Binnacle
from Api.Service.binnacle_service import BinnacleService

# Manejador de errores personalizado
@app.exception_handler(CustomError)
async def unicorn_exception_handler(request: Request, exc: CustomError):
    
    # crear bitácora
    binnacle = Binnacle(
        endpoint=request.url.path,
        method=request.method,
        detail=exc.message,
        status_code=exc.code,
        user_id=1,
        ip_client=request.client.host
    )

    # guardar bitácora
    BinnacleService.create_binnacle(binnacle, db)
    
    error_dict = {
        "code": exc.code,
        "message": exc.message
    }
    
    if exc.details is not None:
      error_dict["details"] = exc.details
    
    return JSONResponse(
        status_code=exc.code,
        content={"error": error_dict},
    )
```
* También se puede dar seguimiento de todas las operaciones de escritura en la base de datos, para ello se puede implementar una tarea en segundo plano en la controller o router de cada modulo. 

## 9. Dependencias
En FastAPI, las dependencias son una herramienta poderosa que te permite desacoplar la lógica de tu aplicación en unidades más pequeñas y reutilizables. Se pueden usar para:
* 1. Inyección de dependencias:
    - Permiten inyectar objetos en tus funciones de ruta y otras funciones de tu aplicación. Esto te permite escribir código más modular y fácil de probar.
    ```
    # inyectar sesión de base de datos
        from fastapi import Depends, FastAPI

        app = FastAPI()

        def get_db_connection():
            # ... 

        @app.get("/")
        async def root(db: Session = Depends(get_db_connection)):
            #  ... 

    ```
* 2. Validación de entrada:
    - Se pueden usar para validar la entrada de las solicitudes a tu API. Puedes crear funciones que validen la entrada y luego usarlas como dependencias en tus funciones de ruta.

    ```
        from fastapi import Depends, FastAPI, HTTPException

        app = FastAPI()

        def validate_user_id(user_id: int):
            if user_id < 1:
                raise HTTPException(status_code=400, detail="El ID del usuario debe ser mayor a 0")

        @app.get("/users/{user_id}")
        async def get_user(user_id: int = Depends(validate_user_id)):
            # ...

    ```
* 3. Autenticación y autorización:
    - Se pueden usar para implementar la autenticación y autorización en tu API. Puedes crear funciones que verifiquen si un usuario está autenticado y autorizado para acceder a un recurso, y luego usarlas como dependencias en tus funciones de ruta.
    ```
        from fastapi import Depends, FastAPI, HTTPException

        app = FastAPI()

        def authenticate_user(username: str, password: str):
            # ...

        def authorize_user(user: User):
            if not user.is_admin:
                raise HTTPException(status_code=401, detail="El usuario no tiene permiso para acceder a este recurso")

        @app.get("/admin")
        async def admin_endpoint(user: User = Depends(authenticate_user, authorize_user)):
            # ... 

    ```

* [Documentación Depends](https://fastapi.tiangolo.com/tutorial/dependencies/)


## 10. Middleware
* El middleware es un código que se ejecuta antes o después de procesar cada solicitud. 

* Consiste en una función que se agrega a la instancia de FastAPI en el archivo principal

* Se aplica a todos los endpoints, sus principales usos son: 
    - Registro y monitoreo de solicitudes
    - Autenticación y autorización
    - Compresión de Respuestas
    - Manejo de Errores
    - Caché de Contenido

```
from fastapi import FastAPI, Request

app = FastAPI()

# Middleware
async def simple_middleware(request: Request, call_next):
    # Codigo ....
    print("Codigo a ejecutar...")

    # Llamar al siguiente middleware o controlador de ruta
    response = await call_next(request)

    return response

# Agregar el middleware a la aplicación
app.middleware("http")(simple_middleware)

# Ruta de ejemplo
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

```

* [Documentación Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)

## 11. Anotaciones
Se utilizan para definir la funcionalidad de las rutas, los modelos de datos y los parámetros de las API.

Las anotaciones son metadatos que se agregan a las funciones, clases y variables para proporcionar información adicional sobre su comportamiento. En FastAPI, las anotaciones se utilizan para definir:

* Rutas: Decoradores como `@app.get` o `@app.post` se utilizan para definir las rutas de la API y el método HTTP asociado.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola mundo!"}

```

* Modelos de datos: Se usan modelos Pydantic para definir la estructura de los datos que se envían y reciben en la API.
```
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

```
* Parámetros: Las anotaciones se usan para definir el tipo de dato, la validación y la descripción de los parámetros de las funciones.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

```
* Respuestas: Se utiliza para indicar un modelo de respuesta o tipo de respuesta
```
from fastapi.responses import JSONResponse

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return JSONResponse(content=item.dict(), status_code=201)


def create_item(item: Item) -> Item:
    return item

def create_dict(item: Item) -> dict:
    return {
        "item": item
    }

def create_str(name: str) -> str:
    return name

```
* Combinación con Depends: para inyectar dependencias en las funciones de la API
```
from fastapi import FastAPI, Depends

app = FastAPI()

async def get_user_from_db(user_id: int) -> User:
    # Obtener el usuario de la base de datos
    ...

@app.get("/users/{user_id}")
async def get_user(user_id: int, user: User = Depends(get_user_from_db)):
    return {"user": user}

```
* Simplificar parámetros: permiten reducir el código repetido de parámetros que es compartido entre rutas

```
from typing_extensions import Annotated

CurrentUser = Annotated[User, Depends(get_current_user)]


@app.get("/items/")
def read_items(user: CurrentUser):
    #código ...


@app.post("/items/")
def create_item(user: CurrentUser, item: Item):
    #código ...


@app.get("/items/{item_id}")
def read_item(user: CurrentUser, item_id: int):
    #código ...


@app.delete("/items/{item_id}")
def delete_item(user: CurrentUser, item_id: int):
    #código ...

```

[Documentación ](https://fastapi.tiangolo.com/release-notes/#0950)

## 12. Tareas en segundo plano
Las tareas en segundo plano en FastAPI son una forma de ejecutar tareas que no necesitan interacción con el usuario. Se pueden usar para realizar tareas que requieren mucho tiempo o que no necesitan ser ejecutadas en tiempo real.

Las tareas en segundo plano en FastAPI se ejecutan en un proceso independiente del proceso principal de la aplicación. Esto significa que no bloquean la interfaz de usuario y no afectan el rendimiento de la aplicación.

Usos: 
* Enviar correos electrónicos.
* Procesar archivos.
* Realizar cálculos complejos.
* Actualizar la base de datos.
* Monitorear la aplicación.

* Ejemplos:

```
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

@app.post("/orders")
async def create_order(order: Order, background_tasks: BackgroundTasks):
    # Crear el pedido en la base de datos
    # código ...

    # Enviar un correo electrónico de confirmación en segundo plano
    background_tasks.add_task(send_confirmation_email, order.email)

def send_confirmation_email(email: str):
    # Enviar el correo electrónico
    # código ...

```

```
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

@app.post("/files")
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    # Guardar el archivo en el disco
    # código ...

    # Procesar el archivo en segundo plano
    background_tasks.add_task(process_file, file.filename)

def process_file(filename: str):
    # Procesar el archivo
    # código ...

```

## 13. Socket
WebSocket es un protocolo de comunicación bidireccional sobre un único socket TCP, diseñado para ser ligero y eficiente. Permite una comunicación en tiempo real entre un cliente y un servidor, lo que lo hace ideal para aplicaciones web interactivas, juegos en línea, aplicaciones de chat, actualizaciones en tiempo real, entre otros casos de uso.

En FastAPI puedes implementar WebSocket fácilmente utilizando las herramientas proporcionadas por Starlette, el marco web subyacente en el que se basa FastAPI.

En FastAPI, los websockets se definen utilizando la función app.websocket(), la cual requiere que se especifique una ruta como argumento. Esta ruta se utiliza para identificar el endpoint del websocket al que los clientes pueden conectarse.

* Crear salas de socket por modulo: para ello deben terminar en `/ws`

* Crear sub-salas de socket para elementos de un modulo, requieren parámetros para identificarlas `/ws/{id}`

* Crear un archivo con la configuración del socket
```
import asyncio
from fastapi import WebSocket
from typing import List

class WebSocketManager:
    def __init__(self):
        self.connections: List = []
        print("WebSocketManager created")
    
    async def connect(self, websocket: WebSocket):
        print("WebSocket connected")
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        print("WebSocket disconnected")
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        await asyncio.gather(
            *[connection.send_text(message) for connection in self.connections]
        )
```

* Implementar el socket en el archivo de ruta del modulo
```

# socket
from fastapi import WebSocket, WebSocketDisconnect,
from Core.Socket.socket_manager import WebSocketManager

# crear manager de websockets
manager = WebSocketManager()

# definir rutas de websockets
# ws://127.0.0.1:8000/api/tags/ws
@tag_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    # Conectar cliente
    await manager.connect(websocket)
    
    print(f"usuarios conectados: {len(manager.connections)}")
    
    try:
        # Escuchar mensajes
        while True:
            
            # Recibir mensaje
            data = await websocket.receive_text()
            print(data)
            
            # Notificar cambios a los clientes
            if data is not None:
                await manager.broadcast(data)
            
    except WebSocketDisconnect:
        # Desconectar cliente
        manager.disconnect(websocket)
        print(f"usuarios conectados: {len(manager.connections)}")

```

* Agregar seguridad al ruta del socket con jwt y permisos
```
from fastapi import WebSocket, WebSocketDisconnect, Header, Depends
from Core.Socket.socket_manager import WebSocketManager
# clase para manejo de permisos
from Core.Security.security_permissions import Permission

# Autorización
def validate_auth( bearer: str = Header(), db: Session = Depends(ConexionBD().get_db)):
   return Permission.verify_role(bearer, ["admin", "user"], db)

# definir rutas de websockets
@tag_router.websocket("/ws", dependencies=[Depends(validate_auth)])
async def websocket_endpoint(websocket: WebSocket, user_data: dict = Depends(validate_auth)):
    #código .....

```

* Identificar cambios en datos en un modulo socket + tareas en segundo plano, agregamos una tarea de segundo plano a los endpoint: create, delete, update.
```
# Manejo de diccionarios en respuesta websocket
import json

# Rutas de tags
@tag_router.post("/")
def create_tag(background_task: BackgroundTasks,  tag: Tag = Body(example=tag_example_create), db: Session = Depends(ConexionBD().get_db)):
    result = TagController.create_tag(tag, db)
    
    if result:
        print("enviando mensaje a los clientes")
        notification_data = {"action": "Create", "module": "tag"}
        background_task.add_task(manager.broadcast, json.dumps(notification_data))
        #background_task.add_task(manager.broadcast, "Se ha creado un nuevo tag")
    
    return result

``` 
* [Documentación WebSocket](https://fastapi.tiangolo.com/advanced/websockets/)
* [Documentación Background Tasks](https://fastapi.tiangolo.com/reference/background/)

## 14. Estaticos
* Requiere el uso de las dependencias 
```
import os
from fastapi.staticfiles import StaticFiles
```
* Configurar las rutas de los archivos
```
resources_path = os.path.join(os.path.dirname(__file__), "Resources/")
app.mount("/Resources", StaticFiles(directory=resources_path), name="Resources")
```

## 15. Template
* Requiere definir como ruta estática la carpeta donde se encuentran
* El uso de variables en los archivos .html
```
{{user_name}} 
```
* Hacer uso de otros achivos como .css, .js, etc...
```
 href={{ url_for('Resources', path='/favicon/favicon-16x16.png') }}
```
* Emplear .html como vista, también requiere la dependencia [Jinja2](#31-manejo-de-archivos-jinja2)
```
# dependencia
from fastapi.templating import Jinja2Templates

# Configurar archivos de vista
views_path = os.path.join(os.path.dirname(__file__), "../../Views/")
views_path = Jinja2Templates(directory=views_path)

# Definir rutas
@home_router.get("/", tags={tag})
def get_home(request: Request):
  return views_path.TemplateResponse("index.html", {"request": request, "title": "Introducción FastAPI"})
```

## 16. Mail
* Requiere la instalación de: [Fastapi Mail](#35-envio-de-correos---fastapi-mail), [dotenv](#33-variables-de-entorno---python-dotenv), [Jinja2](#31-manejo-de-archivos-jinja2), [Email  Validator](#38-validación-de-correo---email-validator)
* Crear un archivo para crear una clase con la configuración y lógica
* Principales importaciones 
```
import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
```
* Configuraciones
```
    conf = ConnectionConfig(
        MAIL_USERNAME=os.getenv("MAIL_USERNAME",""),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD",""),
        MAIL_FROM=os.getenv("MAIL_FROM",""),
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        VALIDATE_CERTS = True
    )
```
* Agregar template a cuerpo de correo
```
    # Renderizar el template HTML
    env = Environment(loader=FileSystemLoader("Resources/Template"))
    template = env.get_template("email.html")
```
* Agregar variables a template
```
    html_content = template.render(
        subject=subject, user_name=user_name, link=link
    )
```
* Adjuntar archivos al correo, mediante el header creamos un CID para agregar directamente la imagen al template, si solo se busca adjuntar archivos los headers no son necesarios
```
    # Obtener la ruta del archivo 
    logo_path = os.path.join(os.path.dirname(__file__), "../../Resources/Images/logo.png")

    # crear un objeto para adjuntar archivo
    adjunto = {
        "file": logo_path,
        "filename": "logo.png",
        "type": "image/png",
        "headers": {
            "Content-ID": "<logo_image>",
        },
    }

    # agregar al objeto de MessageSchema, el atributo de  attachments=[adjunto]
```
* Implementar el archivo adjunto en el template
```
    <img src="cid:logo_image" >

```

* Definir el MessageSchema
```
    email_content = MessageSchema(
        subject=subject,
        recipients=[to],
        body=html_content,
        subtype=MessageType.html,
        attachments=[adjunto],
    )
```
* Enviar mail
```
    fm = FastMail(self.conf)
    await fm.send_message(email_content)
```
* Validar excepciones del formato del correo
```
    # validar el correo antes de agregarlo a MessageSchema
    valid_email = validate_email(to)

    # capturar excepción dentro de un try
        except EmailNotValidError as e:
            raise Exception(f"Error al enviar el correo: {str(e)}")
```

## 17. Manejo de archivos
Almacenamiento de archivos en una carpeta del servidor
* 1: Declarar en el main la ruta de la carpeta Uploads, de manera que se pueda accede a los recursos de que contiene.
```
# importaciones
import os
from fastapi.staticfiles import StaticFiles

# Configurar archivos estáticos
uploads_path = os.path.join(os.path.dirname(__file__), "Uploads/")
app.mount("/Uploads", StaticFiles(directory=uploads_path), name="Uploads")

```
* 2: Uso de la clase UploadFile para el manejo de archivos
```
# importaciones
from fastapi import UploadFile

# ruta
@upload_router.post("/save-upload")
def upload_file2(file: UploadFile):
#...
```

* 3: validaciones del archivo
```
    # validar que hay un archivo
    if not file.filename:
        raise CustomError(400, "No file provided")

    # validar el formato del archivo
    valid_formats = ["image/jpeg", "image/png", "image/jpg"]
    if file.content_type not in valid_formats:
        raise CustomError(400, "Invalid file format")

    # validar el tamaño del archivo
    max_size = 1 * 1024 * 1024
    if file.size > max_size:
        raise CustomError(400, "File size exceeds the limit of 1MB")
```
* 4: Generar un nombre único 
```
    # dependencia
    from uuid import uuid4

    # generar nombre único para cada archivo
    file_name = f"{uuid4()}-{file.filename}"
```

* 5: Guardar el archivo en la carpeta
```
    # guardar el archivo
    file_path = os.path.join("Uploads", file_name)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
        f.close()
```

* 6: Generar url, para acceder a archivo, también esta se puede almacenar en base de datos
```
    # generar url para acceder al archivo
    file_url = f"http://localhost:8000/Uploads/{file_name}"
```
* [Documentación UploadFile](https://fastapi.tiangolo.com/reference/uploadfile/)

* [Documentación OS Files](https://docs.python.org/3/library/os.html#files-and-directories)

* [Documentación uuid](https://docs.python.org/3/library/uuid.html)

## 18. Manejo de Errores
* [Documentación errores](https://fastapi.tiangolo.com/tutorial/handling-errors/#requestvalidationerror-vs-validationerror)

* Manejo de errores personalizados, configurar en el main.py
```
from Core.Validations.custom_error import CustomError
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Manejadores de errores HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {
                "code": exc.status_code, 
                "message": str(exc.detail),
                "url": str(request.url)
            }
        },
    )

# Manejador de errores validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = []
    
    for error in exc.errors():
         errors.append({
            "msg": error["msg"],
            "body": error["loc"][1],
            "input": error["input"]
        })
    
    return JSONResponse(
        status_code=422,
        content={"error": {
            "code": 422, 
            "message": f"Error de validación: {msg}"
            }, 
            "errors": errors,
        }
    )
    
# Manejador de errores personalizado
@app.exception_handler(CustomError)
async def unicorn_exception_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.code,
        content={"error": {"code": exc.code, "message": exc.message}},
    )
```
* crear clase de error personalizado
```
class CustomError(Exception):
  def __init__(self, code, message):
    self.code = code
    self.message = message

  def __str__(self):
    return {
      "error":{
        "code": self.code,
        "message": self.message
      }
    }

```

* Implementar error personalizado ejemplo
```
    def create_task(task: Task, db: Session):
        try:
            # validación de datos
            task.validate_create()
            
            # Crear la tarea
            result = TaskService.create_task(task, db)
            
            # Retornar la respuesta
            return ResponseBase(200, "Task created successfully", result).to_dict()
        except CustomError as e:# Excepciones que validemos
            raise e
        except Exception as e:# Excepciones que no validamos
            raise CustomError(500, f"Error al crear la tarea: {str(e)}")

```

## 19. Encriptado de datos

* Guia de uso
    - 1: Importación
    `
    from passlib.context import CryptContext
    `
    - 2: Crear el contexto de encriptación
    `pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")`
    - 3: Crear el metodo para encryptar contraseñas 
    ```
        @staticmethod
    def hash_password(password: str) -> str:
        return SecurityEncryption.pwd_context.hash(password)
    ```

## 20. Flujo de trabajo de módulos 
* Crear archivo de ruta en Api/Routes/file_router.py
* Agregar los endpoints en el archivo de rutas
* Agregar el router en main.py
* Crear archivo model en Api/Models/file_model.py
* Agregar en archivo de ejemplos los ejemplos del model,  Api/Models/examples.py  
* Crear archivo controller en Api/Controllers/file_controller.py
    - 1 Definir los métodos para cada endpoints
    - 2 Dentro de cada método hacer implementar estructura de control de excepciones 
    - 3 Dentro de cada método hacer validaciones Core/Validations/file_validation.py
    - 4 Dentro de cada método hacer llamado métodos de procesos lógicos
    - 5 Dentro de cada método hacer llamado método del service Api/Service/file_service.py
* Crear archivo service en Api/Service/file_service.py

## 21. Descripción función de packages
#### 21.1 Package Api
* Controllers: se encarga de unir toda la lógica necesaria para cada endpoint
* Data: conexión a base de datos y archivos models schema
* Models: contiene los models para validación de request y examples
* Response: contiene la estructura de la respuesta base de las peticiones
* Routes: contiene los endpoint de cada modulo y la configuraciones que requiera

#### 21.2 Package Resources
Tiene como propósito almacenar en carpetas especificas los recurso internos de la API

#### 21.3 Package Uploads
Tiene como función almacenar todos los archivos de acceso publico 

#### 21.4 Package Views
Contiene las vistas que deseamos implementar en la API

#### 21.5 Package Core
Tiene función principal es contener toda la lógica que la API requiera:
* Validations: validaciones y errores
* Security: permisos, autenticación y encriptación
* Enums: crear tipados personalizados
* Emails: envió de correos
* Files: manejo de archivos


## 22. Relaciones en ORM - Alchemist
#### 22.1 One to Many
Relación de uno a muchos.
* Requiere importar 
```
from sqlalchemy import ForeignKey
```
* Definir una columna para el id, indicando el nombre de la tabla y el atributo id
```
user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
```
* Aplicar un join para obtener los datos de la relación, crear un atributo con el nombre en singular de la tabla con la que tiene una relación, agrega como parámetro el nombre de la clase data o model schema
```
category_task= relationship("CategoryTask", lazy="joined")
```
#### 22.2 One to Many Inverse
La relación inversa permite recuperar datos desde la clase que no tiene la foreignkey como un arreglo de todos los registros asociados.

* Agregar en la relación de muchos, la propiedad: back_populates y ligarla a una variable para aplicar la relación inversa y recuperar los registros asociados
```
 # TaskData
 category_task= relationship("CategoryTasksData", lazy="joined", back_populates="tasks")
```

* Agregar en la relación de uno, una variable tasks, para insertar los registros asociados
```
# CategoryTasksData
 tasks = relationship("TaskData",lazy="joined", back_populates="category_task")
```
#### 22.3 Many to Many
En este tipo de relación se requieren dos tablas y una tabla intermedia para establecer las relaciones de muchos a muchos. 
* Crear en data un archivo pivot.data para tablas intermedias
```
# dependencias
from sqlalchemy import Table, Column, ForeignKey, Integer
# importaciones
from Api.Data.conection import ConexionBD

# tabla intermedia o pivote
tasks_tags = Table(
    "tasks_tags",
    ConexionBD.Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)
```
* Aplicar relación many to many, para ello se agrega una linea en el file_data.py

```
class TaskData(ConexionBD.Base):
    __tablename__ = "tasks"
    ...
    # relacion many to many, con tabla intermedia o pivote 
    tasks = relationship("TaskData", secondary=tasks_tags, back_populates="tags")
    
```
* Para ejecutar la relación y obtener listado de registros relacionados
```
# obtener la tarea
_task = db.query(TaskData).get(task_id)

# obtener etiquetas asociadas a la tarea
_task.tags
```
* Para ejecutar la relación y agregar registros relacionados
```
# obtener la tarea
_task = db.query(TaskData).get(task_id)

# obtener la etiqueta
_tag = db.query(TagData).get(tag_id)

# asociar ambas en la tabla intermedia
_task.tags.append(_tag)

# guardar cambios
db.commit()
```
* Para ejecutar la relación y remover registros relacionados
```
# obtener la tarea
_task = db.query(TaskData).get(task_id)

# obtener la etiqueta
_tag = db.query(TagData).get(tag_id)

# remover la etiqueta de la tabla intermedia que asocia ambas tablas
 _task.tags.remove(_tag)

# guardar cambios
db.commit()

```
* Se recomienda validar la existencia de task, tag y que ambas estén relacionadas
```
# validar que existe la tarea
_task = db.query(TaskData).get(task_id)
if _task is None:
    raise CustomError(404, "Task not found")

# validar que existe la tag
_tag = db.query(TagData).get(tag_id)
if _tag is None:
    raise CustomError(404, "Tag not found")

# validar que hay una asociación task - tag
if _tag not in _task.tags:
    raise CustomError(404, "Tag not found in task")

```
#### 22.4 Relaciones Documentación
* [Documentación Relationship](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

## 23. Variables de entorno
Se requiere el uso de la dependencia [Python Dotenv](#33-variables-de-entorno---python-dotenv)

* Crear archivo .env
* Definir en el archivo.env mis variables de entorno
* Declaración de las variables de entorno
```
VARIABLE_NOMBRE=valor_variable
```
* Uso de variables de entorno
```
# dependencia
from dotenv import load_dotenv

# iniciar dotenv
load_dotenv()

variable = os.getenv("VARIABLE_ENTORNO", "valor por defecto - opcional")
```


## 24. Notación de ellipsis
En Python es un objeto especial que se utiliza como marcador o como un indicador de "relleno" en ciertas estructuras de datos o funciones. Su función principal es indicar que algo está faltando o que se espera que se llene más tarde.

En FastApi se utiliza en los parámetros de la ruta y en los modelos, en  para indicar un valor obligatorio, esto sustituye un posible valor por defecto.
```
# Ejemplo en rutas
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}/posts/{*post_ids}")
async def get_posts(
    user_id: int = Path(..., gt=0),
    post_ids: List[int] = Path(..., min_items=1)
):
    # código ...

    return {"user_id": user_id, "post_ids": post_ids}

```
```
# Ejemplo en Modelos
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(...)
    description: str | None = Field(default=None)
    tags: List[str] = Field(default=[])

class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    items: List[Item] = Field(default=[])

```



## 25. Lista de errores HTTP
| Código | Estado | Descripción |
|---|---|---|
|2XX| ✅ | Exitosa |
| 200 | OK | La solicitud se completó con éxito. |
| 201 | Created | Se ha creado un nuevo recurso. |
|3XX| ↪️ | Redirección |
| 301 | Moved Permanently | El recurso solicitado se ha movido permanentemente a una nueva ubicación. |
| 302 | Found | El recurso solicitado se ha encontrado temporalmente en una nueva ubicación. |
|4XX| ❌ |Error del cliente|
| 400 | Bad Request | La solicitud del cliente es malformed. |
| 401 | Unauthorized | El cliente no está autorizado para acceder al recurso solicitado. |
| 403 | Forbidden | El cliente tiene prohibido acceder al recurso solicitado. |
| 404 | Not Found | El recurso solicitado no se encuentra en el servidor. |
| 408 | Request Timeout | El tiempo de espera se agotado |
| 422 | Unprocessable Entity | La solicitud no se puede procesar debido a errores en la entidad. |
|5XX| 🟥 |Error del servidor|
| 500 | Internal Server Error | Se ha producido un error inesperado en el servidor. |
| 503 | Service Unavailable | El servidor no está disponible temporalmente. |

## 26. Problemas con rutas
Si tienes errores a la hora de realizar peticiones y te piden parámetros que la url no tiene pero otras si lo tienen pueden intentar una de las siguientes posibles soluciones: 

* Ordenar las rutas desde la que no tienen parámetro en la url, luego las que tienen parámetros en la url de forma descendente 
![alt text](./Resources/Images/solucion-rutas-1.jpg)

* Agrear un / al final de cada ruta que tiene parámetros en la url
![alt text](./Resources/Images/solucion-rutas-2.jpg)

## 27. Problemas con el Interprete
Si no reconoce el interprete debes elegirlo de forma manual.

![alt text](./Resources/Images/bug-interprete-1.png)

![alt text](./Resources/Images/bug-interprete-2.png)

## 28. Problemas con alembic
Puede suceder que al trabajar en cooperativo o al perder un archivo de migración o al borrar una migración suelen presentarse errores que indica en terminal donde se ejecuta el servidor que no encuentra el head con un id, para solucionar este problema se debe eliminar los archivos de las migraciones, tambien eliminar el registro de la tabla.

![alt text](./Resources/Images/error-alembic-migration.png)

![alt text](./Resources/Images/error-alembic-bd.png)
