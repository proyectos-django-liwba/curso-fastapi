# Dependencias
import os
from uuid import uuid4
from typing import List
from fastapi import APIRouter, File, UploadFile

# Importaciones
from Core.Validations.custom_error import CustomError
from Api.Models.upload_model import Upload
from Core.Files.file import FileManager

# crear el router
upload_router = APIRouter()

#! el parametro ... indica que es requerido u obligatorio

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


@upload_router.post("/form-upload")
def upload_files3( upload: Upload ):

  try:
    # validar que hay un objeto
    if not upload:
        raise CustomError(400, "No data provided")
    
    # validar que hay un archivo
    if not upload.image:
        raise CustomError(400, "No image provided")

    image = FileManager.convert_base64_to_image(upload.image)
    type_image = FileManager.get_type_image(upload.image)
    content_type = FileManager.get_content_type(upload.image)
    size_image = len(image)
    
    # validar el formato del archivo
    valid_formats = ["image/jpeg", "image/png", "image/jpg"]
    if content_type not in valid_formats:
        raise CustomError(400, "Invalid file format")
      
    # validar el tamaño del archivo
    max_size = 1 * 1024 * 1024
    if size_image > max_size:
        raise CustomError(400, "File size exceeds the limit of 1MB")

    # generar nombre unico para el archivo
    file_name = f"{uuid4()}.{type_image}"

    # guardar el archivo
    file_path = os.path.join("Uploads", file_name)    
    FileManager.save_image(image, file_path)
    upload.image = f"http://localhost:8000/Uploads/{file_name}"
    return upload 

  except CustomError as e:
      raise e
  except Exception as e:
      raise CustomError(500, f"Error al subir los archivos: {e}")
