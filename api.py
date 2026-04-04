from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get ("/")
def home ():
    return{"Message": "🛠 Welcome to Secure Image Share API!"}

@app.post ("/upload")
def upload_image(file: UploadFile = File(...)):
    return{"Filename": file.filename}

