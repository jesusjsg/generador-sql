from fastapi import FastAPI
from src.core.config import settings

print(settings.model_dump_json(indent=2))

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Test"}
