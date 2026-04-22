from fastapi import FastAPI

# routes
from routes.dummy import router as dummy_router

app = FastAPI()

app.include_router(dummy_router)