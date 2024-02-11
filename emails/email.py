# sistema operativo
import os
# dependencias

# errores
from domain.error import CustomError
# variables de entorno
from dotenv import load_dotenv



class EmailManager: 
    """ conf = ConnectionConfig(
        MAIL_USERNAME="your_username",
        MAIL_PASSWORD="your_password",
        MAIL_FROM="your_email@gmail.com",
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_TLS=True,
        MAIL_SSL=False,
    ) """

async def send_email(self, to: str, subject: str, message: str ):
    try:

        
        return {"message": "Email sent"}
    except CustomError as e:
        raise e
    except Exception as e:
        raise CustomError(500, f"Error al enviar el correo: {str(e)}")

