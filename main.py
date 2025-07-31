from fastapi import FastAPI, HTTPException, Request, Response, status, Depends
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI()

posts = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime


@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"

@app.get("/home", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome home!</h1>"

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return HTMLResponse(content="<h1>404 NOT FOUND</h1>", status_code=404)

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(new_posts: List[Post]):
    posts.extend(new_posts)
    return posts