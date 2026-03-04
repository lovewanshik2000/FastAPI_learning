from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    data = {
        "status":"Success",
        "message":"Hello World!"
    }
    return data

@app.get("/about")
def about():
    data = {
        "status":"Success",
        "message":"This is a simple API built with FastAPI."
    }
    return data