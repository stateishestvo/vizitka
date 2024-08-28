from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the business card API"}