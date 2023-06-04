from fastapi import FastAPI
from app.api.router import router

app = FastAPI()

# Include the router in your FastAPI application
app.include_router(router)