from domain.error import CustomError
import base64
import re

class FileManager:
    def convert_base64_to_image(data):

        try:
            #remueve el prefijo data:image/png;base64,
            match = re.match(r'data:image/\w+;base64,(.*)', data)
          
            if not match:
                raise CustomError(400, "Invalid base64 format")
              
            # convert base64 to image
            imageData = base64.b64decode( match.group(1) )

            return imageData

        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al convertir en archivo: {str(e)}")
          
    def get_content_type(data):
        try:
            extract_str = data.split(",")[0]
            match = re.match(r'data:(.*);base64', extract_str)
            
            if not match:
                raise CustomError(400, "Invalid base64 format")
              
            print(match.group(1))
            return match.group(1)
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al obtener el tipo de archivo: {str(e)}")
          
    def get_type_image(data):
        try:
            match = re.match(r'data:image/(\w+);base64,(.*)', data)
            if not match:
                raise CustomError(400, "Invalid base64 format")
              
            print(match.group(1))
            return match.group(1)
        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al obtener el tipo de archivo: {str(e)}")

    def save_image(image, path):
        try:
            with open(path, "wb") as f:
                f.write(image)
                f.close()

        except CustomError as e:
            raise e
        except Exception as e:
            raise CustomError(500, f"Error al guardar la imagen: {str(e)}")