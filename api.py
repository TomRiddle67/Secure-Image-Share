from fastapi import FastAPI, UploadFile, File
import shutil
import os
from storage import save_image


app = FastAPI()

@app.get ("/")
def home ():
    return{"Message": "🛠 Welcome to Secure Image Share API!"}

@app.post ("/upload")
def upload_image(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image_id = save_image(temp_path)
    os.remove(temp_path)

    return{"image_id": image_id}

