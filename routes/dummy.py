from fastapi import APIRouter

# kafka
from service.util.Kafka import producer

# idempotency
import uuid

# util
from service.util.SQLite import query, execute

router = APIRouter(prefix="/dummy", tags=["Rotas de teste"])

@router.get("/")
def dummy_function():
    return {"message": "Esta é uma rota de teste."}


@router.post("/send")
def send_message(message: str, idempotency_key: str = None):
    if idempotency_key is None:
        idempotency_key = str(uuid.uuid4())
    
    try:
        # Verificar se a chave de idempotência já foi processada
        existing = query("SELECT * FROM idempotency_keys WHERE key = ?", (idempotency_key,))
        if existing:
            return {"status": "Chave de idempotência já processada"}
        
        # Salvar a chave de idempotência para evitar reprocessamento
        execute("INSERT INTO idempotency_keys (key) VALUES (?)", (idempotency_key,))
    except Exception as e:
        print(f"Erro ao processar a chave de idempotência: {e}")
        return {
            "status": "duplicado",
            "message": "Requisição já processada"
        }
    
    event = {
        "id": idempotency_key,
        "event": "dummy_event",
        "payload": {
            "message": message
        }
    }
    producer.send("dummy-topic", event)

    return {
        "status": "Mensagem enviada para Kafka",
        "idempotency_key": idempotency_key
    }
