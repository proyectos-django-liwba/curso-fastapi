# Guía de FastAPI 2024 
[![FastAPI](./assets/images/fastapi.png)](https://fastapi.tiangolo.com/)

* Wilfredo Barquero Herrera
    - [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](liwbarqueroh@gmail.com )
    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/liwBh)
* Elmer Mejias Carranza
    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ing-Elmer)
    - [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://elmermejias47@gmail.com)


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
    - 📁**Validaciones**: validaciones - enums
    - 📁**File**: manejo de archivos
    - 📁**Email**: manejo de emails 
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

##### Estructura de carpetas:
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

[Problemas con el Interprete](#problemas-con-el-interprete)



* [Documentación oficial](https://fastapi.tiangolo.com/)

## 1.1 - Crear entorno virtual = env
* Crear env: `python -m venv ./env/env1`
* Activar env linux: `source env/env1/bin/activate`
* Activar env windows: `./env/env1/Scripts/activate`
* [Documentación oficial](https://docs.python.org/es/3/library/venv.html)
* Revisar que esté instalado: `pip list`
* Revisar version de python: `python -V`
* Actualizar pip: `python.exe -m pip install --upgrade pip`

## 1.2 - Instalar dependencias
* Instalar FastAPI: `pip install fastapi`
* Instalar sevidor = Uvicorn: `pip install uvicorn`
* Instalar dependencias: `pip install -r requirements.txt`
* Crear archivo requirements.txt: `pip freeze > requirements.txt`
* Revisar dependencias: `pip freeze`

## 1.3 - Crear servidor
* Crear servidor: `uvicorn main:app --reload`
* Crear servidor con puerto: `uvicorn main:app --reload --port 8000`
* Crear servidor con nombre y host: `uvicorn main:app --reload --port 8000 --host 0.0.0.0`

## 1.4 - Instalar dependencia Jinja2
* Instalar dependencia: `pip install jinja2`
* descripción: `Jinja2 es un motor de plantillas para Python. Es rápido, ampliamente utilizado y seguro.`
* [Documentación oficial](https://pypi.org/project/Jinja2/)

## 1.5 - Instalar dependencia SQLAlchemy
* Instalar dependencia: `pip install sqlalchemy`
* descripción: `SQLAlchemy es un kit de herramientas SQL para Python.`
* [Documentación oficial](https://www.sqlalchemy.org/)


* [Documentación oficial](https://pypi.org/project/autopep8/)

## 1.7 - Instalar dependencia pydantic
* Instalar dependencia: `pip install pydantic`
* descripción: `Pydantic es una librería para validar datos en Python.`
* [Documentación Validaciones](https://docs.pydantic.dev/latest/concepts/validators/) 
* [Documentación Tipos de datos](https://docs.pydantic.dev/1.10/usage/types/#pydantic-types)
* Instalar validacion de email: `pip install pydantic[email]`

## 1.8 - Instalar dependencia python-dotenv
* Instalar dependencia: `pip install python-dotenv`
* descripción: `python-dotenv lee variables de entorno desde archivos .env.`
* [Documentación oficial](https://pypi.org/project/python-dotenv/)

## 1.9 - Instalar dependencia python-multipart
* Instalar dependencia: `pip install python-multipart`
* descripción: `python-multipart es una librería para manejar datos multipart en Python.`
* [Documentación oficial](https://pypi.org/project/python-multipart/)
* [Documentación Uploadfile](https://fastapi.tiangolo.com/reference/uploadfile/)

## 1.10 - Instalar dependencia fastapi-mail
* Instalar dependencia: ```pip install fastapi-mail```
* descripción: es una librería para el envió de correos
* [Documentación](https://sabuhish.github.io/fastapi-mail/example/)

# 2.0 Base de datos
* Cada base de datos requiere un conector que se debe instalar de forma independiente. Luego configurar la conexión con esa base de datos.

## 2.1 instalar dependencia sqlalchemy
* instalar dependencia: ```pip install sqlalchemy```
* [Documentación Instalación](https://docs.sqlalchemy.org/en/20/intro.html#installation)
* [Documentación Guía](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

## 2.2 instalar dependencia  para base de datos
#### 2.2.1 BD Postgre SQL
* instalar dependencia: ```pip install psycopg2 ```
* [Documentación](https://www.psycopg.org/docs/install.html#quick-install)

#### 2.2.1 BD MySQL conector
* instalar dependencia: ```pip install mysql-conector-python ```

## 2.3 instalar dependencia  para Hasheo de contraseña 
* Instalar dependencia: ```pip install passlib[bcrypt]```
* [Docuementación passlib](https://passlib.readthedocs.io/en/stable/)
* [Docuementación ](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-passlib)

## 2.4 instalar dependencia  para migraciones alembic
* instalar dependencia:```pip install alembic ```
* [Documentación](https://alembic.sqlalchemy.org/en/latest/)

#### Configuracion
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

# 3.0 Auth JWT

# 4.0 Permisos

# 5.0 Bitacora

# Dependencias

# Middleware

# Anotaciones

# 6.0 Microservicios

# 7.0 Socket

# Mail

# Template

# Errores

# Estaticos

# Manejo de archivos

#### Comandos alembic
* Crear migración: ```alembic revision --autogenerate -m "nombre-migracion"```
* Aplicar la ultima migración: ```alembic upgrade head```


### Lista de errores HTTP
![alt text](./assets/images/http-errores-1.png)

![alt text](./assets/images/http-errores-2.png)


### Problemas con el Interprete 
![alt text](./assets/images/bug-interprete-1.png)

![alt text](./assets/images/bug-interprete-2.png)