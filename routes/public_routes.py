from fastapi import APIRouter

public_router = APIRouter()

@public_router.get("/articles")
def get_articles():
    articles = [
        {
            "title": "Sleep",
            "description": "And why it's over rated",
            "link": "/article/sleep"
        },
        {
            "title": "Nutrition",
            "description": "blah blah",
            "link": "/article/nutrition"
        }
    ]

    return articles

