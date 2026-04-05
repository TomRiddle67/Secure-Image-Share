from fastapi import FastAPI, UploadFile, File, HTTPException, Security
import shutil
import os
from storage import save_image, get_image
from fastapi.responses import FileResponse
from fastapi.security import APIKeyHeader
from config import IMAGES_DIR, API_KEYS


app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_key(api_key: str = Security(api_key_header)):
    if api_key not in API_KEYS:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid or missing API key"
        )
    return api_key

@app.get ("/")
def home ():
    return{"Message": "🛠 Welcome to Secure Image Share API!"}

@app.post ("/upload")
def upload_image(
    file: UploadFile = File(...), 
    api_key: str = Security(verify_key)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image_id = save_image(temp_path)
    os.remove(temp_path)

    return{"image_id": image_id}

@app.get("/get/{image_id}")
def retrieve_image(image_id: str):
    path = get_image(image_id)
    if path:
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")





