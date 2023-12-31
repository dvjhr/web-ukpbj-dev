from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("base.html", context)