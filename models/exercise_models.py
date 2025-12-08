from pydantic import BaseModel, EmailStr


class AddExerciseForm(BaseModel):
    user_email: EmailStr
    date: str
    exercise: str
    weight: float
    reps: int


class GetByDate(BaseModel):
    user_email: EmailStr
    date: str
