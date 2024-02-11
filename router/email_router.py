from fastapi import APIRouter


# Create a router
email_router = APIRouter()

# Define a route

@email_router.post("/send-email")
def send_email():
    print("Send email")
    return {"message": "Email sent"}