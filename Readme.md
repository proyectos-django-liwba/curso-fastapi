# Template FastAPI 2024


## Desarrolladores 

* 🧑‍💻Wilfredo Barquero Herrera

    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/liwBh)

    - [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wilfredo-barquero-herrera-17bb29258)


* 👨‍💻Elmer Mejias Carranza

    - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ing-Elmer)

    - [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ermer-mejias-carranza-a36b39232)


## Código implementado 

* Paginación 
* Envió de correo 
* JWT
* WebSocket
* Migraciones
* Errores personalizados
* Archivos estáticos
* Carga de archivos
* Bitácora 


## Crear entorno virtual
* Crear el un entorno virtual
```
python -m venv ./env/env1
```
* Activar el entorno virtual
```
./env/env1/Scripts/activate
```

## Instalar dependencias 
* Instalar todas las dependencias definidas en el archivo requirements.txt del template
```
pip install -r requirements.txt
```

## Iniciar y configurar Alembic
* Iniciar Alembic en el proyecto: 
```alembic init alembic```
* Ubicación de migraciones generadas: ``alembic/versions/``
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