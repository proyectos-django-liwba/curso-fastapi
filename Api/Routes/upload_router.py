# Dependencias
import os
from uuid import uuid4
from typing import List
from fastapi import APIRouter, File, UploadFile, Body, Depends
from sqlalchemy.orm import Session
# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.upload_model import Upload
from Api.Models.examples import upload_example_create, upload_example_update
from Api.Controllers.upload_controller import UploadController
from Api.Data.conection import ConexionBD

# crear el router
upload_router = APIRouter()

# definir rutas
@upload_router.post("/file")
def upload_file(file: bytes = File(...)):
    return {"file": len(file)}

@upload_router.post("/upload")
def upload_file1(file: UploadFile):
    return {
        "file_name": file.filename,
        "content_type": file.content_type,
    }

@upload_router.post("/save-upload")
def upload_file2(file: UploadFile):
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

    # generar nombre unico para cada archivo
    file_name = f"{uuid4()}-{file.filename}"

    # guardar el archivo
    file_path = os.path.join("Uploads", file_name)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
        f.close()

    # generar url para acceder al archivo
    file_url = f"http://localhost:8000/Uploads/{file_name}"

    return {
        "url": file_url
    }

@upload_router.post("/multi-upload")
def upload_files3(files: List[UploadFile] = File(...)):

    try:
        # validar que hay archivos
        if not files[0].filename:
            raise CustomError(400, "No files provided")

        # validar la cantidad de archivos
        if len(files) > 5:
            raise CustomError(400, "You can only upload up to 5 files")

        # Validar el formato y el tamaño de los archivos
        valid_formats = ["image/jpeg", "image/png", "image/jpg"]
        max_size = 1 * 1024 * 1024
        for file in files:
            # Validar el formato
            if file.content_type not in valid_formats:
                raise CustomError(400, "Invalid file format")

            # Validar el tamaño
            if file.size > max_size:
                raise CustomError(400, "File size exceeds the limit of 1MB")

        # Almacenar los archivos
        file_urls = []

        for file in files:
            # Generar nombre único y almacenar el archivo
            file_name = f"{uuid4()}-{file.filename}"
            file_path = os.path.join("Uploads", file_name)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
                f.close()

            # Almacenar la URL del archivo
            file_url = f"http://localhost:8000/Uploads/{file_name}"
            file_urls.append(file_url)

        return {"file_urls": file_urls}

    except CustomError as e:
        raise e

    except Exception as e:
        raise CustomError(500, f"Error al subir los archivos: {e}")

# crud de archivos con base de datos
@upload_router.post("/image_base64")
def upload_image( upload: Upload = Body(example=upload_example_create), db: Session = Depends(ConexionBD().get_db)):
    return UploadController.create_upload(upload, db)
    
@upload_router.get("/{upload_id}")
def get_upload(upload_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UploadController.get_upload(upload_id, db)

@upload_router.get("/by_user_id/{user_id}")
def get_upload_by_user_id(user_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UploadController.get_upload_by_user_id(user_id, db)

@upload_router.put("/")
def update_upload(upload: Upload = Body(example=upload_example_update), db: Session = Depends(ConexionBD().get_db)):
    return UploadController.update_upload(upload, db)

@upload_router.delete("/{upload_id}")
def delete_upload(upload_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UploadController.delete_upload(upload_id, db)