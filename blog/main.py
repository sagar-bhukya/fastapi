from fastapi import FastAPI
from pydantic import BaseModel
from .import models
from .database import engine
from .models import Blog

app=FastAPI()
models.Base.metadata.create_all(engine)

@app.post('/bog')
def create(blog:Blog):
    return blog