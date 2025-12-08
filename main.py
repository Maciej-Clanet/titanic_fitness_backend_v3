from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import auth_router
from routes.public_routes import public_router
from routes.exercise_routes import exercise_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(public_router, prefix="/public", tags=["Public"])
app.include_router(exercise_router, prefix="/exercise", tags=["Exercises"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
