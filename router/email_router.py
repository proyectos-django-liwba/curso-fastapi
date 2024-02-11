from fastapi import APIRouter
from emails.email import EmailManager

# Create a router
email_router = APIRouter()

# Define a route
@email_router.post("/send-email")
async def send_email():
    otp = "1da-sd22DA-SDAD-A3DASDA-4"
    to= "shinigamiliw@gmail.com"
    subject= "Prueba"
    user_name= "Wilfredo"
    link = f"http://localhost:5173/{otp}"
    
    # enviar correo
    email_manager = EmailManager()
    await email_manager.send_email(to,subject,user_name,link)
    
    return {"message": "Email enviado"}
    