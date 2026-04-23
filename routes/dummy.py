from fastapi import APIRouter

# kafka
from service.util.Kafka import producer

router = APIRouter(prefix="/dummy", tags=["Rotas de teste"])

@router.get("/")
def dummy_function():
    return {"message": "Esta é uma rota de teste."}


@router.post("/send")
def send_message(message: str):
    event = {
        "event": "dummy_event",
        "payload": {
            "message": message
        }
    }
    producer.send("dummy-topic", event)
    return {"status": "Mensagem enviada para Kafka"}
