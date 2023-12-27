from fastapi import FastAPI
from app.api import random_generator

app = FastAPI()

app.include_router(random_generator.router, prefix="/random_array_generator", tags=["random_array"])