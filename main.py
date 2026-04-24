from fastapi import FastAPI
from prometheus_client import Counter, Histogram

# routes
from routes.dummy import router as dummy_router
from routes.metrics import router as metrics_router


app = FastAPI()

app.include_router(dummy_router)
app.include_router(metrics_router)