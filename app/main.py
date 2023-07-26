from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .schemas.data_model import Card

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    dummy_card = Card(
        distance_from_london=100,
        past_employers=2,
        qualifications=50,
        emojis_in_profile=0,
    )
    message = "The best way to be found professionally"
    return templates.TemplateResponse(
        "index.html",
        {
            "title": f"Linkder: {message}",
            "request": request,
            "message": message,
            **dummy_card.model_dump(),
        },
    )
