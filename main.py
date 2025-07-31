from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"