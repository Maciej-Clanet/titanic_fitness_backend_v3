from fastapi import APIRouter, HTTPException 
from models.auth_models import LoginForm, RegisterForm 

auth_router = APIRouter() 

@auth_router.post("/register") 
def register(register_data: RegisterForm): 
    new_user = register_data.model_dump() 
    return new_user 

@auth_router.post("/login") 

def login(login_data: LoginForm): 
    email = login_data.email    
    return {"temp": "temp"} 
