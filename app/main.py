import srsly
import filetype
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
app.mount("/images", StaticFiles(directory="app/data/images"), name="images")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def form(request:Request, myName:str = Form(''),nameOfBusiness: str = Form(''),latlong:str = Form(''), textOfAdvertisement: str= Form(''),notes:str =Form(''),message:str=Form(''), file: Union[UploadFile, None] = None):
    valid_file = "no image"
    if file.filename != "":
        contents = await file.read()
        kind = filetype.guess(contents)
        if kind.mime == 'image/jpeg' or kind.mime == 'image/png':
            valid_file = datetime.now().strftime("%Y-%m-%d-%H:%M:%S") +"_" + file.filename
            (images_dir / valid_file).write_bytes(contents)
    data = {"nameOfBusiness": nameOfBusiness, 
            "myName":myName,
            "latlong":latlong, 
            "textOfAdvertisement": textOfAdvertisement, 
            "notes":notes,
            "message":message,
            "filename": valid_file}
    srsly.write_json((data_dir / f'{current_counter}_{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.json'), data)
    data["request"] = request
    return templates.TemplateResponse("success.html", data)

@app.get('/results')
async def results(request:Request): 
    results = []
    for d in data_dir.iterdir():
        a = srsly.read_json(d)
        results.append(a)
    return templates.TemplateResponse("results.html", {"results":results, "request":request})

@app.get('/data')
async def results(request:Request): 
    results = []
    for d in data_dir.iterdir():
        a = srsly.read_json(d)
        results.append(a)
    return results
