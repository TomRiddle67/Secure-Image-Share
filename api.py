from fastapi import FastAPI

app = FastAPI()

@app.get ("/")
def home ():
    return{"Message": "🛠 Welcome to Secure Image Share API!"}

