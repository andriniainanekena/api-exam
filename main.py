from fastapi import FastAPI, HTTPException, Request, Response, status, Depends
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"

@app.get("/home", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome home!</h1>"

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return HTMLResponse(content="<h1>404 NOT FOUND</h1>", status_code=404)

