from fastapi import FastAPI
from src.routes import notes_router

app = FastAPI()
app.include_router(notes_router)
