from fastapi import APIRouter, HTTPException 
from models.auth_models import LoginForm, RegisterForm, UserPublicData
from db import db 

auth_router = APIRouter() 

users = db["users"]  # reference to the collection 

@auth_router.post("/register", response_model=UserPublicData) 
def register(register_data: RegisterForm): 
    
    if users.find_one({"email": register_data.email}): 
        raise HTTPException(status_code=400, detail="Email already exists") 
    
    newUser = { 
        "email": register_data.email, 
        "password": register_data.password,  # not secure, NEVER DO THIS IN REAL WORLD 
        "username": register_data.username, 
    } 
    result = users.insert_one(newUser)
    print(result) 

    return {"email": register_data.email, "username": register_data.username} 

@auth_router.post("/login", response_model=UserPublicData) 
def login(login_data: LoginForm): 
    
    foundUser = users.find_one({"email" : login_data.email})

    if not foundUser or foundUser["password"] !=  login_data.password:
        raise HTTPException(status_code=401, detail="Invalid Credentials Goober")

    return {
        "username" : foundUser["username"],
        "email" : foundUser["email"]
    } 
