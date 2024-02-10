# Sección 1 - Curso de Python FastAPI

## 0 FastAPI
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

### Lista de errores HTTP
![alt text](image.png)

![alt text](image-1.png)