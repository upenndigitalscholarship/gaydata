import srsly
from datetime import datetime
from typing import Union
from pathlib import Path
from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

data_dir = Path.cwd() / 'app' / 'data' / 'json'
assert data_dir.exists()
current_counter = len(list(data_dir.iterdir()))

images_dir = Path.cwd() / 'app' / 'data' / 'images'
assert images_dir.exists()

app = FastAPI()
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def form(request:Request, myName:str = Form(''),nameOfBusiness: str = Form(''),latlong:str = Form(''), textOfAdvertisement: str= Form(''),notes:str =Form(''),message:str=Form(''), file: Union[UploadFile, None] = None):
    if file.filename != "":
        contents = await file.read()
        (images_dir / (datetime.now().strftime("%Y-%m-%d-%H:%M:%S") +"_" + file.filename)).write_bytes(contents)
    data = {"nameOfBusiness": nameOfBusiness, 
            "myName":myName,
            "latlong":latlong, 
            "textOfAdvertisement": textOfAdvertisement, 
            "notes":notes,
            "message":message, 
            "filename":file.filename}
    srsly.write_json((data_dir / f'{current_counter}_{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.json'), data)
    data["request"] = request
    return templates.TemplateResponse("success.html", data)
