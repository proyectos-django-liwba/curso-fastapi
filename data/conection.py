# sistema operativo
import os
# variables de entorno
from dotenv import load_dotenv
# dependencias 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class ConexionBD:
    DB_USERNAME= os.getenv("DB_USERNAME")
    DB_PASSWORD= os.getenv("DB_PASSWORD")
    DB_HOST= os.getenv("DB_HOST")
    DB_NAME= os.getenv("DB_NAME")
    
    def __init__(self):#constructor
        # Configuración de la base de datos
        #PostgresSQL 16
        self.DATABASE_URL = f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.DB_NAME}"
        # Crear el motor de la base de datos
        self.Engine = create_engine(self.DATABASE_URL)
        # Crear la sesión de la base de datos
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.Engine)
        # Crear la base de datos
        self.Base = declarative_base()
        
    def create_tables(self):
        try:  
            self.Base.metadata.create_all(self.Engine)
            print("Tablas creadas")
        except Exception as e:
            print(f"Error al crear las tablas: {str(e)}")
        
    def drop_tables(self):
        try:
            self.Base.metadata.drop_all(self.Engine)
            print("Tablas eliminadas")
        except Exception as e:
            print(f"Error al eliminar las tablas: {str(e)}")
        
    def get_engine(self):
        return self.Engine
    
    def get_base(self):
        return self.Base
    
    def get_Session(self):
        return self.SessionLocal
    
    def close_Session(self):
        self.SessionLocal.close_all()

    # Obtener la sesión de la base de datos
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    def verificar_conexion(self):
        try:
            with self.Engine.connect():
                print("Conexión exitosa")
                return True
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False