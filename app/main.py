# tdd-project/app/main.py

from fastapi import FastAPI, Depends
from app.config import Settings, get_Settings

app = FastAPI()

@app.get("/ping")
async def pong(settings: Settings = Depends(get_Settings)):
    return {"ping" : "pong! pong! pong!",
            "environment" : settings.environment,
            "testing" : settings.testing            
            }


