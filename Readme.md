# Guía de FastAPI 2024 
[![FastAPI](./Resources/Images/fastapi.png)](https://fastapi.tiangolo.com/)


## Desarrolladores 
![coders](./Resources/Images/coders.png)
* 🧑‍💻Wilfredo Barquero Herrera
     [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](liwbarqueroh@gmail.com )
     [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/liwBh)
* 👨‍💻Elmer Mejias Carranza
     [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ing-Elmer)
     [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://elmermejias47@gmail.com)


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
* [Arquitectura de proyecto](#arquitectura-de-proyecto)
    - [1.Descripción de las capas](#1.-descripción-de-las-capas:)
    - [2. Estructura de carpetas](#2.-estructura-de-carpetas:)
* [FastAPI](#1-fastapi)
* [Iniciar proyecto](#2-iniciar-proyecto)
    - [Iniciar proyecto](#21-crear-proyecto)
    - [Iniciar proyecto](#22-crear-servidor)
    - [Iniciar proyecto](#23-comandos-de-inicio-servidor)
* [Instalación de dependencias](#3-instalación-de-dependencias)
    - [Jinga2](#31-manejo-de-archivos-jinja2)
    - [SqlAlchemy](#32-orm---sql-sqlalchemy)
    - [Pydantic](#33-validación-pydantic)
    - [Python Multipart](#34-manejo-de-archivos---python-multipart)
    - [Fastapi Mail](#35-envio-de-correos---fastapi-mail)
    - [Passlib](#36-hasheo-de-contraseña-passlib)
    - [Alembic](#37-migraciones-alembic)
* [Base de datos](#4-base-de-datos)
    - [Conector Postgre](#411-conector-bd-postgre-sql)
    - [Conector Mysql](#412-conector-bd-mysql)
* [Migraciones](#5-migraciones)
    - [Iniciar proyecto](#51-configuración-alembic)
    - [Iniciar proyecto](#52-comandos-alembic)
* [Auth JWT](#6-auth-jwt)
* [Permisos](#7-permisos)
* [Bitácora](#8-bitacora)
* [Dependencias](#9-dependencias)
* [Middleware](#10-middleware)
* [Anotaciones](#11-anotaciones)
* [Microservices](#12-microservicios)
* [Socket](#13-socket)
* [Mail](#14-mail)
* [Template](#15-template)
* [Estáticos](#16-estaticos)
* [Manejo de archivos](#17-manejo-de-archivos)
* [Manejo de errores](#18-manejo-de-errores)
* [Encriptado de datos](#19-encriptado-de-datos)
* [Lista de errores HTTP](#lista-de-errores-http)
* [Problemas con el Interprete](#problemas-con-el-interprete)

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

#### 3.3 Variables de entorno - Python Dotenv
* Instalar dependencia: 
```
pip install python-dotenv
```
* Descripción: python-dotenv lee variables de entorno desde archivos .env.

* [Documentación python-dotenv](https://pypi.org/project/python-dotenv/)

#### 3.4 Manejo de archivos - Python Multipart
* Instalar dependencia: 
```
pip install python-multipart
```

* Descripción: python-multipart es una librería para manejar datos multipart en Python.
* [Documentación python-multipart](https://pypi.org/project/python-multipart/)
* [Documentación Uploadfile](https://fastapi.tiangolo.com/reference/uploadfile/)

#### 3.5 Envio de correos - Fastapi Mail
* Instalar dependencia: 
```
pip install fastapi-mail
```
* Descripción: es una librería para el envió de correos
* [Documentación fastapi-mail](https://sabuhish.github.io/fastapi-mail/example/)

#### 3.6  Hasheo de contraseña Passlib
* Instalar dependencia: ```pip install passlib[bcrypt]```
* [Docuementación passlib](https://passlib.readthedocs.io/en/stable/)
* [Docuementación Guía](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-passlib)

#### 3.7  Migraciones Alembic
* Configurar las variables de entorno en un archivo .env
    ```* Instalar dependencia:```pip install alembic ```
* [Documentación alembic](https://alembic.sqlalchemy.org/en/latest/)


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

## 7. Permisos

## 8. Bitacora

## 9. Dependencias

## 10. Middleware

## 11. Anotaciones

## 12. Microservicios

## 13. Socket

## 14. Mail

## 15. Template

## 16. Estaticos

## 17. Manejo de archivos

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

## 21. Descripción función de package Api
* Controllers: se encarga de unir toda la lógica necesaria para cada endpoint
* Data: conexión a base de datos y archivos models schema
* Models: contiene los models para validación de request y examples
* Response: contiene la estructura de la respuesta base de las peticiones
* Routes: contiene los endpoint de cada modulo y la configuraciones que requiera

## 21. Descripción función de package Resources
Tiene como propósito almacenar en carpetas especificas los recurso internos de la API

## 22. Descripción función de package Uploads
Tiene como función almacenar todos los archivos de acceso publico 

## 23. Descripción función de package Views
Contiene las vistas que deseamos implementar en la API

## 23. Descripción función de package Core
Tiene función principal es contener toda la lógica que la API requiera:
* Validations: validaciones y errores
* Security: permisos, autenticación y encriptación
* Enums: crear tipados personalizados
* Emails: envió de correos
* Files: manejo de archivos

### Lista de errores HTTP
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
| 422 | Unprocessable Entity | La solicitud no se puede procesar debido a errores en la entidad. |
|5XX| 🟥 |Error del servidor|
| 500 | Internal Server Error | Se ha producido un error inesperado en el servidor. |
| 503 | Service Unavailable | El servidor no está disponible temporalmente. |


### Problemas con el Interprete
Si no reconoce el interprete debes elegirlo de forma manual.

![alt text](./Resources/Images/bug-interprete-1.png)

![alt text](./Resources/Images/bug-interprete-2.png)