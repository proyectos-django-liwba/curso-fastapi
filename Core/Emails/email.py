# dependencias
import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
# Importaciones
from Core.Validations.custom_error import CustomError

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class EmailManager:
    # Configuración de mail
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

    async def send_email(self, to: str, subject: str, user_name: str, link: str = "http://localhost:5173", type: int = 1):
        try:
            # validar el correo
            valid_email = validate_email(to)
            to = valid_email.email

            # Renderizar el template HTML
            env = Environment(loader=FileSystemLoader("Resources/Template"))
            template = env.get_template("activate_account.html")
            if type == 2:
                 template = env.get_template("recovery_password.html")
            

            html_content = template.render(
                subject=subject, user_name=user_name, link=link
            )

            # Obtener la ruta del archivo 
            logo_path = os.path.join(os.path.dirname(__file__), "../../Resources/Images/FastAPI.avif")

            # Validar que el archivo exista
            if not os.path.exists(logo_path):
                raise CustomError(500, "El archivo del logo no existe")

            # Crear el adjunto
            adjunto = {
                "file": logo_path,
                "filename": "logo.png",
                "type": "image/png",
                "headers": {
                    "Content-ID": "<logo_image>",
                },
            }

            # Crear el mensaje
            email_content = MessageSchema(
                subject=subject,
                recipients=[to],
                body=html_content,
                subtype=MessageType.html,
                attachments=[adjunto],
            )

            # Enviar el mensaje
            fm = FastMail(self.conf)
            await fm.send_message(email_content)

        except CustomError as e:
            raise e
        except EmailNotValidError as e:
            raise CustomError(400, f"El correo {to} no es válido")
        except Exception as e:
            raise CustomError(500, f"Error al enviar el correo: {str(e)}")
