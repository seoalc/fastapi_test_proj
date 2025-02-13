from fastapi import FastAPI

from app.api.router import router as router_api

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Success!"}

app.include_router(router_api)