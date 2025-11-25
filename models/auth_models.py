from pydantic import BaseModel


class RegisterForm(BaseModel):
    email: str
    password: str
    username: str


class LoginForm(BaseModel):
    email: str
    password: str


class UserPublicData(BaseModel):
    email: str
    username: str
