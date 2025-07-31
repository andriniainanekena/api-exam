from fastapi import FastAPI, HTTPException, Request, Response, status, Depends
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"

@app.get("/home", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome home!</h1>"
