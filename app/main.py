from fastapi import FastAPI, Request

from app.routers import router

app = FastAPI()


@app.get('/')
def hello():
    return {"Hello": "World"}
