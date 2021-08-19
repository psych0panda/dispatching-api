from typing import Optional
import os

from fastapi import FastAPI
import uvicorn
from app.models.database import database

from app.api.api_v1.api import api_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000, reload=True, debug=False, workers=1)
