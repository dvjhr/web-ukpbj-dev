from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.get("/")
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("beranda.html", context)

@app.get("/{page_name}")
def any_page(request: Request, page_name: str):
    return templates.TemplateResponse(f"{page_name}.html", context={"request":request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)