from typing import Union
from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def form(nameOfBusiness: str = Form(),latlong:str = Form(), textOfAdvertisement: str= Form(),notes:str =Form(),message:str=Form(), file: Union[UploadFile, None] = None):
    if not file:
        return {"nameOfBusiness": nameOfBusiness, "latlong":latlong, "textOfAdvertisement": textOfAdvertisement, "notes":notes, "message":message}
    else:
        return {"filename": file.filename}
