import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "running"}

@app.get("/movies")
def get_movies():
    return [
        {"id": 1, "name": "Avengers"},
        {"id": 2, "name": "Batman"}
    ]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port)
