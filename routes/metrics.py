from fastapi import APIRouter, Response

# metrics
from prometheus_client import generate_latest

router = APIRouter(prefix="/metrics", tags=["Rotas de teste"])


@router.get("/")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@router.get("/custom")
def custom_metrics():
    from service.util.Metrics import REQUEST_COUNT, REQUEST_TIME
    import time

    REQUEST_COUNT.inc()

    with REQUEST_TIME.time():
        time.sleep(0.5)

    return {"status": "ok"}