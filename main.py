import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    name: str

movies = [
    {"id": 1, "name": "Avengers"},
    {"id": 2, "name": "Batman"}
]

@app.get("/")
def home():
    return {"message": "running"}

@app.get("/movies")
def get_movies():
    return movies

@app.post("/movies")
def create_movie(movie: Movie):
    new_id = max(m["id"] for m in movies) + 1 if movies else 1
    new_movie = {"id": new_id, "name": movie.name}
    movies.append(new_movie)
    return new_movie

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port)
