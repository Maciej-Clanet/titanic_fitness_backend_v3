from datetime import datetime
from fastapi import APIRouter, HTTPException
from models.exercise_models import AddExerciseForm, GetByDate
from db import db

exercise_router = APIRouter()
exercises = db["exercises"]


@exercise_router.post("/add")
def add_exercise(form: AddExerciseForm):
    doc = {
        "user_email": form.user_email,
        "date": form.date,
        "exercise": form.exercise,
        "weight": form.weight,
        "reps": form.reps,
        "created_at": datetime.now(),
    }
    result = exercises.insert_one(doc)
    return {"ok": True}


@exercise_router.post("/bydate")
def get_by_date(data: GetByDate):

    results = exercises.find(
        {"user_email": data.user_email, "date": data.date},
    ).sort("created_at", 1)

    grouped = {}
    for ex in results:
        item = {
            "id": str(ex["_id"]),
            "exercise": ex["exercise"],
            "weight": ex["weight"],
            "reps": ex["reps"],
            "date": ex["date"],
            "created_at": ex.get("created_at"),
        }
        exercise_name = ex["exercise"]

        grouped.setdefault(exercise_name, [])
        grouped[exercise_name].append(item)

    print(grouped)
    return {"date": data.date, "groups": grouped}
